#!/usr/bin/env python3
"""
FreeStyle Libre / LibreView の CSV から血糖指標を計算する。
使い方: python analyze_libre.py <libre.csv> [--chart out.png]
出力: 指標をJSONで標準出力。--chart 指定時はAGP風の時刻別中央値/範囲グラフも保存。

非糖尿病・ウェルネス文脈の目安を併記するが、判定は libre.md のルールに従うこと。
指標の意味・目標値・鑑別は references/functional-tests/libre.md を参照。
"""
import sys, json, argparse
import pandas as pd, numpy as np

GLU_KEYS = ["履歴グルコース", "Historic Glucose", "グルコース値(mg", "Glucose"]
SCAN_KEYS = ["スキャングルコース", "Scan Glucose"]
TS_KEYS = ["タイムスタンプ", "Timestamp", "時刻", "Time"]

def find_header_and_read(path):
    # ヘッダ行（グルコース列を含む行）を探して読み込む
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        lines = f.readlines()
    header_idx = 0
    for i, ln in enumerate(lines[:10]):
        if any(k in ln for k in GLU_KEYS) and any(k in ln for k in TS_KEYS):
            header_idx = i
            break
    df = pd.read_csv(path, skiprows=header_idx, encoding="utf-8-sig")
    return df

def pick_col(df, keys):
    for c in df.columns:
        if any(k.lower() in str(c).lower() for k in keys):
            return c
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--chart", default=None)
    args = ap.parse_args()

    df = find_header_and_read(args.csv)
    ts_col = pick_col(df, TS_KEYS)
    glu_col = pick_col(df, GLU_KEYS)
    scan_col = pick_col(df, SCAN_KEYS)
    if ts_col is None or glu_col is None:
        print(json.dumps({"error": "グルコース列またはタイムスタンプ列を特定できませんでした",
                          "columns": list(map(str, df.columns))}, ensure_ascii=False))
        sys.exit(1)

    t = pd.to_datetime(df[ts_col], errors="coerce")
    g = pd.to_numeric(df[glu_col], errors="coerce")
    if scan_col is not None:  # 履歴が無い行はスキャン値で補完
        g = g.fillna(pd.to_numeric(df[scan_col], errors="coerce"))
    d = pd.DataFrame({"t": t, "g": g}).dropna().sort_values("t").reset_index(drop=True)
    if len(d) < 20:
        print(json.dumps({"error": "有効なグルコースデータが少なすぎます", "n": int(len(d))}, ensure_ascii=False))
        sys.exit(1)

    g = d["g"].values
    hours = d["t"].dt.hour + d["t"].dt.minute/60
    days = (d["t"].max() - d["t"].min()).days + 1
    mean = float(np.mean(g)); sd = float(np.std(g, ddof=1))
    cv = float(sd/mean*100)
    gmi = 3.31 + 0.02392*mean  # GMI(%) 推定A1c
    def pct(mask): return float(np.mean(mask)*100)
    metrics = {
        "期間日数": int(days), "測定点数": int(len(g)),
        "平均血糖_mgdl": round(mean,1), "SD": round(sd,1), "変動係数CV_pct": round(cv,1),
        "推定GMI_pct": round(gmi,2), "最小": int(np.min(g)), "最大": int(np.max(g)),
        "TIR_70_140_pct": round(pct((g>=70)&(g<=140)),1),
        "TIR_70_180_pct": round(pct((g>=70)&(g<=180)),1),
        "TAR_over140_pct": round(pct(g>140),1),
        "TAR_over180_pct": round(pct(g>180),1),
        "TBR_under70_pct": round(pct(g<70),1),
        "TBR_under54_pct": round(pct(g<54),1),
        "夜間00_06_平均": round(float(np.mean(g[(hours>=0)&(hours<6)])),1) if np.any((hours>=0)&(hours<6)) else None,
        "夜間00_06_最小": int(np.min(g[(hours>=0)&(hours<6)])) if np.any((hours>=0)&(hours<6)) else None,
        "起床前03_08_平均": round(float(np.mean(g[(hours>=3)&(hours<8)])),1) if np.any((hours>=3)&(hours<8)) else None,
    }
    # 反応性低血糖の疑い: 食後帯(11-22時)にピーク後の急落で<70に触れる回数
    low_events = int(np.sum((g<70)&(hours>=10)&(hours<23)))
    metrics["日中低血糖_70未満_件"] = low_events
    # 変動の大きさ（スパイク傾向）
    metrics["140超の割合_pct"] = round(pct(g>140),1)

    out = {"metrics": metrics, "columns_used": {"timestamp": str(ts_col), "glucose": str(glu_col)}}
    print(json.dumps(out, ensure_ascii=False, indent=2))

    if args.chart:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        for fam in ["Noto Sans CJK JP", "IPAexGothic", "Yu Gothic", "Hiragino Sans"]:
            try:
                matplotlib.font_manager.findfont(fam, fallback_to_default=False)
                plt.rcParams["font.family"] = fam; break
            except Exception:
                continue
        plt.rcParams["axes.unicode_minus"] = False
        hb = (d["t"].dt.hour + d["t"].dt.minute/60)
        bins = np.arange(0,24.5,0.5)
        idx = np.digitize(hb, bins)-1
        med=[]; p10=[]; p90=[]; xs=[]
        for b in range(len(bins)-1):
            vals=g[idx==b]
            if len(vals)>0:
                med.append(np.median(vals)); p10.append(np.percentile(vals,10)); p90.append(np.percentile(vals,90)); xs.append(bins[b])
        plt.figure(figsize=(9,4))
        plt.fill_between(xs,p10,p90,alpha=.2,color="#33658A",label="10-90%")
        plt.plot(xs,med,color="#2F4858",lw=2,label="中央値")
        plt.axhline(140,color="#C19A1F",ls="--",lw=1); plt.axhline(70,color="#b04a3a",ls="--",lw=1)
        plt.xlabel("時刻"); plt.ylabel("mg/dL"); plt.title("時刻別 血糖プロファイル（AGP風）")
        plt.xticks(range(0,25,3)); plt.legend(); plt.tight_layout(); plt.savefig(args.chart,dpi=130)
        print(f"[chart saved] {args.chart}", file=sys.stderr)

if __name__ == "__main__":
    main()
