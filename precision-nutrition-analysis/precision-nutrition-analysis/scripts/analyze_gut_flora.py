#!/usr/bin/env python3
"""
腸内フローラ検査の菌組成CSVから、多様性・主要グループの割合を計算する。
使い方: python analyze_gut_flora.py <taxa.csv>
CSVは「taxon(菌名), relative_abundance(相対存在比%)」列を含むこと（level列は任意）。
門(phylum)と属(genus)が混在してもよい（門はF/B比、属はグループ集計に使う）。

出力: 指標をJSONで標準出力。判定の意味・注意は
references/functional-tests/gut-flora.md を参照。
※ 腸内細菌の解釈は相関・仮説段階が多い。数値は目安であり断定に使わない。
"""
import sys, json, math
import pandas as pd

# 属→機能グループの対応（代表例。検査により菌名表記が異なるので部分一致で拾う）
BENEFICIAL = ["bifidobacterium", "lactobacillus", "akkermansia"]
SCFA_BUTYRATE = ["faecalibacterium", "roseburia", "blautia", "eubacterium", "coprococcus", "butyric"]
OPPORTUNISTIC = ["escherichia", "klebsiella", "proteobacteria", "bilophila", "desulfovibrio",
                 "enterobacter", "shigella", "fusobacterium"]
PHYLA = ["firmicutes", "bacteroidetes", "actinobacteria", "proteobacteria", "verrucomicrobia"]

def col(df, keys):
    for c in df.columns:
        if any(k in str(c).lower() for k in keys):
            return c
    return None

def main():
    if len(sys.argv) < 2:
        print("usage: analyze_gut_flora.py <taxa.csv>"); sys.exit(1)
    df = pd.read_csv(sys.argv[1], encoding="utf-8-sig")
    tcol = col(df, ["taxon", "菌", "name", "taxa", "genus", "門", "属"])
    acol = col(df, ["abundance", "存在", "割合", "%", "ratio", "percent", "rel"])
    if tcol is None or acol is None:
        print(json.dumps({"error": "菌名列または存在比列を特定できません",
                          "columns": list(map(str, df.columns))}, ensure_ascii=False)); sys.exit(1)
    d = df[[tcol, acol]].copy()
    d.columns = ["taxon", "ab"]
    d["ab"] = pd.to_numeric(d["ab"], errors="coerce")
    d = d.dropna()
    d["low"] = d["taxon"].astype(str).str.lower()

    def grp_sum(keys):
        m = d["low"].apply(lambda s: any(k in s for k in keys))
        return float(d.loc[m, "ab"].sum())

    # 門レベルでF/B比
    phyla = {p: grp_sum([p]) for p in PHYLA}
    fb = (phyla["firmicutes"] / phyla["bacteroidetes"]) if phyla["bacteroidetes"] > 0 else None

    # Shannon多様性（属レベルの相対存在比から。門行は多様性計算から概ね除外するため属候補を優先）
    genus = d[~d["low"].isin(PHYLA)]
    if len(genus) >= 3:
        p = genus["ab"].values
        p = p / p.sum()
        shannon = float(-sum(x*math.log(x) for x in p if x > 0))
        richness = int((genus["ab"] > 0).sum())
    else:
        shannon = None; richness = None

    metrics = {
        "多様性_Shannon": round(shannon, 2) if shannon is not None else None,
        "検出属数_目安": richness,
        "門構成_pct": {k: round(v, 1) for k, v in phyla.items() if v > 0},
        "FB比_Firmicutes÷Bacteroidetes": round(fb, 2) if fb else None,
        "有用菌_合計pct": round(grp_sum(BENEFICIAL), 1),
        "酪酸産生菌_合計pct": round(grp_sum(SCFA_BUTYRATE), 1),
        "日和見_有害候補_合計pct": round(grp_sum(OPPORTUNISTIC), 1),
    }
    notes = []
    if shannon is not None and shannon < 2.0:
        notes.append("多様性が低めの可能性（食物繊維の種類・発酵食品を増やす方向）")
    if metrics["酪酸産生菌_合計pct"] < 8:
        notes.append("酪酸産生菌が少なめの可能性（レジスタントスターチ・水溶性食物繊維）")
    if metrics["有用菌_合計pct"] < 5:
        notes.append("ビフィズス菌等の有用菌が少なめの可能性（オリゴ糖・発酵食品）")
    if metrics["日和見_有害候補_合計pct"] > 10:
        notes.append("日和見・有害候補がやや多い可能性（要因の見直し・必要なら医師）")
    print(json.dumps({"metrics": metrics, "注記_目安": notes,
                      "免責": "腸内細菌の解釈は相関・仮説段階が多い。数値は目安であり断定に用いない。"},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
