#!/usr/bin/env python3
"""
出力物に薬機法・医療広告まわりの禁止表現が混入していないかを検査するリンター。

Step 6（安全チェック）で `check_deidentification.py` と並べて実行する。
判断基準は `references/expression-guard.md`。

使い方:
    python3 scripts/check_expressions.py /mnt/user-data/outputs/
    python3 scripts/check_expressions.py report.docx report.md

対象: .md .txt .json .csv .docx（本文テキストを抽出）
終了コード: 0=クリーン（ERRORなし）, 1=ERRORあり
           ※ WARN は終了コードに影響しない。目視で判断する。

注意: このスクリプトを skill ディレクトリ自身に対して走らせると、
      expression-guard.md（禁止語の一覧そのもの）が大量に引っかかる。
      検査対象は出力物のみ。
"""
import sys, os, re, zipfile, glob

# ---- ERROR: 例外なく直す ------------------------------------------------------
ERROR_PATTERNS = [
    ("治癒をうたう",
     r'(治り(ます|ました)|治る(?!み)|完治|治癒|根治)'),
    ("治療行為と読める",
     r'(を治療(し|する|します)|に効く治療)'),
    ("効果の断定",
     r'(効きます|効果があります|効果的です|効果は絶大)'),
    ("変化の断定",
     r'[がはを](改善|解消|消失)(します|しました|されます)'),
    ("予防の断定",
     r'([がはを](予防|防止)(します|できます)|防げます)'),
    ("例外なしの含意",
     r'((絶対に|確実に|誰でも)(治|改善|効|良く|下が|上が|痩せ)|副作用は(ありません|ない|一切))'),
    ("100%表現",
     r'(100\s*[%％]の(方|人|方々)|100\s*[%％]\s*(改善|効果|安全))'),
    ("体験談で治癒を示唆",
     r'(治った方|良くなった方|完治した)'),
    # --- 既存の禁止表現（output-checklist.md §3 と同一） ---
    ("ビタミンDの感染予防",
     r'(ビタミンD|25[-‐]?OHD)[^。]{0,20}(感染|風邪|インフルエンザ)[^。]{0,10}(予防|防)'),
    ("サブグループでの有効性",
     r'サブグループ[^。]{0,20}(有効性が確認|効果が確認|効果があ)'),
    ("やせ菌・デブ菌",
     r'(やせ菌|痩せ菌|デブ菌)'),
    ("遺伝子と疾患の断定",
     r'(この|その)遺伝子[^。]{0,10}(だから|があるから)[^。]{0,10}(病|症|になり)'),
    ("生物学的年齢の若返り",
     r'(生物学的年齢が[^。]{0,6}(若|下が)|(サプリ|補充)[^。]{0,12}若返)'),
]

# ---- WARN: 文脈しだい。目視で判断する ------------------------------------------
WARN_PATTERNS = [
    ("断定気味の変化表現",
     r'[がはを](軽減|正常化|回復)(します|されます)'),
    ("効能をうたう慣用句",
     r'(免疫力(を|が)?(アップ|上が|高め)|代謝が上がり|デトックス|毒素を(出|排出))'),
    ("優劣の比較",
     r'(より効果|最も効果的|他(社|院)より)'),
    ("必ず（定型文以外）",
     r'必ず(?![^。]{0,20}(主治医|医師|医療専門職|かかりつけ|ご相談|相談))'),
]

# ---- 添え書きの有無チェック（文書全体で1回） --------------------------------------
EFFECT_MENTION = re.compile(r'(改善|変化が|期待でき|効果|良くな)')
INDIVIDUAL_NOTE = re.compile(r'(個人差|人により|人によって|一様では)')
MEDICAL_MENTION = re.compile(r'(服用|お薬|服薬|治療中|通院|処方)')
DOCTOR_NOTE = re.compile(r'(主治医|かかりつけ医|医療専門職)')


def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".docx":
            with zipfile.ZipFile(path) as z:
                parts = [n for n in z.namelist()
                         if n.startswith("word/") and n.endswith(".xml")]
                buf = []
                for n in parts:
                    xml = z.read(n).decode("utf-8", "ignore")
                    xml = re.sub(r'</w:p>', "\n", xml)
                    buf.append(re.sub(r'<[^>]+>', '', xml))
                return "\n".join(buf)
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"  ! 読めませんでした: {path} ({e})")
        return ""


def check_file(path):
    """(errors, warns) を返す。各要素は (行番号, ラベル, 抜粋)"""
    text = extract_text(path)
    if not text:
        return [], []
    lines = text.splitlines()
    errors, warns = [], []

    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        for label, pat in ERROR_PATTERNS:
            for m in re.finditer(pat, line):
                errors.append((i, label, snippet(line, m)))
        for label, pat in WARN_PATTERNS:
            for m in re.finditer(pat, line):
                warns.append((i, label, snippet(line, m)))

    # 文書全体の添え書きチェック
    if EFFECT_MENTION.search(text) and not INDIVIDUAL_NOTE.search(text):
        warns.append((0, "個人差の注記が見当たらない",
                      "効果・変化に触れているが「個人差」の一文がない"))
    if MEDICAL_MENTION.search(text) and not DOCTOR_NOTE.search(text):
        warns.append((0, "主治医相談の一文が見当たらない",
                      "服薬・治療の話題があるが「主治医にご相談ください」がない"))

    return errors, warns


def snippet(line, m, width=22):
    s = max(0, m.start() - width)
    e = min(len(line), m.end() + width)
    out = line[s:e].strip()
    return ("…" if s > 0 else "") + out + ("…" if e < len(line) else "")


def collect(targets):
    files = []
    exts = {".md", ".txt", ".json", ".csv", ".docx"}
    for t in targets:
        if os.path.isdir(t):
            for p in glob.glob(os.path.join(t, "**", "*"), recursive=True):
                if os.path.isfile(p) and os.path.splitext(p)[1].lower() in exts:
                    files.append(p)
        elif os.path.isfile(t):
            files.append(t)
        else:
            print(f"  ! 見つかりません: {t}")
    return sorted(set(files))


def main():
    targets = sys.argv[1:] or ["/mnt/user-data/outputs/"]
    files = collect(targets)
    if not files:
        print("検査対象のファイルがありません。")
        return 0

    total_e = total_w = 0
    for path in files:
        errors, warns = check_file(path)
        if not errors and not warns:
            continue
        print(f"\n■ {path}")
        for ln, label, sn in errors:
            loc = f"L{ln}" if ln else "全体"
            print(f"  [要修正] {loc} {label}: {sn}")
        for ln, label, sn in warns:
            loc = f"L{ln}" if ln else "全体"
            print(f"  [確認]   {loc} {label}: {sn}")
        total_e += len(errors)
        total_w += len(warns)

    print(f"\n--- 検査 {len(files)} ファイル / 要修正 {total_e} 件 / 確認 {total_w} 件 ---")
    if total_e:
        print("要修正が残っています。`references/expression-guard.md` の言い換え表で直してください。")
    elif total_w:
        print("要修正なし。確認項目は文脈しだいなので目視で判断してください。")
    else:
        print("クリーンです。")
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main())
