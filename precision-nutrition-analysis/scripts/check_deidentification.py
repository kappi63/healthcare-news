#!/usr/bin/env python3
"""
出力物に個人識別情報が混入していないかを検査するリンター。

Step 6（安全チェック）で必ず実行する。目視では見落とすため機械的に走らせる。

使い方:
    python3 scripts/check_deidentification.py /mnt/user-data/outputs/
    python3 scripts/check_deidentification.py report.docx report.md

対象: .md .txt .json .csv .docx（本文テキストを抽出）／ファイル名そのもの
終了コード: 0=クリーン, 1=要確認の検出あり
"""
import sys, os, re, json, zipfile, glob

# ---- 検出パターン -----------------------------------------------------------
PATTERNS = [
    ("生年月日", r'(生年月日|生年|誕生日|DOB)[\s:：*_｜|・]{0,8}(19[0-9]{2}|20[0-2][0-9])[/年\-\.](0?[1-9]|1[0-2])'),
    ("電話番号",           r'(?<![\w\-.:/;])0\d{1,3}[-(]\d{1,4}[-)]\d{3,4}(?![\w\-.:/])'),
    ("メールアドレス",     r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}'),
    ("郵便番号",           r'(?<![\w\-.:/])〒\s?\d{3}-\d{4}(?![\w\-.:/])'),
    ("住所（丁目番地）",   r'[都道府県市区町村][^\s、。]{0,12}?\d+[-−丁目]\d+'),
    ("保険者/被保険者番号", r'(保険者番号|被保険者番号|記号\s*[:：]|番号\s*[:：])\s*\d{4,}'),
    ("カルテ/検体番号",     r'(カルテ|診察券|患者|検体|受付)\s*(No\.?|番号|ID)\s*[:：]?\s*[A-Za-z0-9\-]{4,}'),
    ("マイナンバーらしき12桁", r'(?<!\d)\d{12}(?!\d)'),
]

# 警告レベル（終了コードには影響しない）
WARN_PATTERNS = [
    ("日付が日単位", r'(19[0-9]{2}|20[0-2][0-9])[/年\-\.](0?[1-9]|1[0-2])[/月\-\.](0?[1-9]|[12][0-9]|3[01])[日]?'),
]

# 氏名の疑い: 「〇〇様」の〇〇がプレースホルダでない場合
# 「さん」は「たくさん」等の誤検出が多いため対象外。レポートの呼びかけは「様」で統一されている。
NAME_HONORIFIC = re.compile(r'([^\s、。「」（）\{\}]{2,12})\s*(様(?![付々式子])|氏(?!名))')
PLACEHOLDER = "{{CLIENT_NAME}}"
# 氏名でないことが明らかな語（誤検出の除外）
NAME_ALLOW = {"あなた", "皆", "ご本人", "クライアント", "患者", "利用者", "お客",
              "施術者", "本人", "同", "多", "各", "一", "この", "その", PLACEHOLDER}
# 「〜様」「〜氏」で名詞を作るが人名ではない語の直前字
NOT_NAME_PREFIX = set("多同模仕王神皆各異一殿奥若様態体摂華某分容")

# ファイル名から先に除去してよい正規の要素（症例ID・年月・年月日）
CASE_ID = re.compile(r'PN-\d{4}-\d{3}')
ISO_DATE = re.compile(r'\d{4}-\d{2}(-\d{2})?')


def normalize_filename(base):
    """症例IDと日付を伏せてから検査する（正規の要素を誤検出しないため）"""
    b = CASE_ID.sub("<CASEID>", base)
    b = ISO_DATE.sub("<DATE>", b)
    return b


def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".docx":
            with zipfile.ZipFile(path) as z:
                parts = [n for n in z.namelist()
                         if n.startswith("word/") and n.endswith(".xml")]
                xml = "".join(z.read(n).decode("utf-8", "ignore") for n in parts)
            return re.sub(r"<[^>]+>", "", xml)
        if ext in (".md", ".txt", ".json", ".csv", ".html"):
            return open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        return f"__READ_ERROR__ {e}"
    return None


def check_file(path):
    findings = []
    warnings = []
    base = os.path.basename(path)

    # --- ファイル名 ---
    fname = normalize_filename(base)
    for cand, hon in NAME_HONORIFIC.findall(fname):
        cand = re.split(r'[_\-\s.]', cand)[-1]          # 区切りの後ろだけを氏名候補に
        if cand and cand not in NAME_ALLOW:
            findings.append(("ファイル名", f"氏名の疑い: {cand}{hon}"))
    for label, pat in PATTERNS:
        if re.search(pat, fname):
            findings.append(("ファイル名", label))

    # --- 本文 ---
    text = extract_text(path)
    if text is None:
        return findings, warnings
    if text.startswith("__READ_ERROR__"):
        findings.append(("読込", text))
        return findings, warnings

    for label, pat in PATTERNS:
        for m in re.finditer(pat, text):
            snippet = text[max(0, m.start() - 20):m.end() + 20].replace("\n", " ")
            findings.append((label, f"…{snippet}…"))

    for label, pat in WARN_PATTERNS:
        for m in re.finditer(pat, text):
            snippet = text[max(0, m.start() - 15):m.end() + 15].replace("\n", " ")
            warnings.append((label, f"…{snippet}… ／ 採血は年月までで足りる"))

    clean = re.sub(r'[*_#>`|]+', ' ', text)
    for m in NAME_HONORIFIC.finditer(clean):
        cand = m.group(1)
        if cand in NAME_ALLOW or PLACEHOLDER in cand:
            continue
        if cand[-1] in NOT_NAME_PREFIX:          # 多様・同様・摂氏 等
            continue
        if any(cand.endswith(a) for a in NAME_ALLOW):   # 「〜クライアント様」等
            continue
        cand = cand[-6:]                          # 前方の文脈を氏名候補にしない
        if cand.endswith("}}"):          # {{CLIENT_NAME}}様
            continue
        snippet = clean[max(0, m.start() - 15):m.end() + 15].replace("\n", " ")
        findings.append(("氏名の疑い", f"{cand}{m.group(2)} … 「{snippet}」"))

    # --- プレースホルダの存在確認（レポート本文のみ） ---
    is_meta = any(k in text[:400] for k in ("テスト結果", "回帰テスト", "統合テスト", "変更履歴"))
    if not is_meta and any(k in base for k in ("レポート", "report", "Report")):
        if PLACEHOLDER not in text:
            warnings.append(("プレースホルダ不在", f"{PLACEHOLDER} が本文にない（実名の可能性・要目視）"))

    return findings, warnings


def collect(targets):
    files = []
    for t in targets:
        if os.path.isdir(t):
            for p in glob.glob(os.path.join(t, "**", "*"), recursive=True):
                if os.path.isfile(p):
                    files.append(p)
        elif os.path.isfile(t):
            files.append(t)
    return files


def main():
    targets = sys.argv[1:] or ["/mnt/user-data/outputs"]
    files = collect(targets)
    if not files:
        print("検査対象のファイルがありません。")
        return 0

    total = warn_total = 0
    for path in sorted(files):
        findings, warns = check_file(path)
        total += len(findings)
        warn_total += len(warns)
        if findings or warns:
            tag = "要修正" if findings else "警告"
            print(f"\n[{tag}] {path}")
            for label, detail in findings:
                print(f"   ✗ {label}: {detail}")
            for label, detail in warns:
                print(f"   △ {label}: {detail}")
        else:
            print(f"[OK] {os.path.basename(path)}")

    print("\n" + "=" * 60)
    print(f"要修正 {total} 件 ／ 警告 {warn_total} 件（{len(files)}ファイル）")
    if total:
        print("✗ 識別子の混入あり。除去してから納品すること。")
        return 1
    if warn_total:
        print("△ 警告のみ。内容を目視確認のうえ納品可。")
    else:
        print("✓ クリーン。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
