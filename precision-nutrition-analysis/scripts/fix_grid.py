#!/usr/bin/env python3
"""
Word（日本語）の行グリッド起因のレイアウト崩れを、生成済み .docx に後処理で当てるスクリプト。

日本語の Word 文書は既定で「行グリッド」に段落を吸着させる（sectPr の docGrid）。
このため、フォントサイズや行間を指定しても**グリッド1行分に切り上げられ**、
行間が意図より広がる／表や見出しの直後が不自然に空く／ページ末で改ページがずれる、
といった崩れが起きる。Node の `docx` ライブラリで生成した文書でも同じ。

使い方:
    python3 scripts/fix_grid.py report.docx              # 上書きで修正
    python3 scripts/fix_grid.py report.docx -o fixed.docx
    python3 scripts/fix_grid.py report.docx --check      # 診断のみ（書き換えない）
    python3 scripts/fix_grid.py report.docx --docgrid-off # セクションのグリッド自体も無効化

既定の動作:
  1. styles.xml の docDefaults に `<w:snapToGrid w:val="0"/>` を入れ、全段落に効かせる
  2. document.xml 内で明示的に snapToGrid=1 になっている段落を 0 に落とす
  3. lineRule="auto" の行間指定を**報告する**（自動では変えない。下記の理由）

`--docgrid-off` を付けると、sectPr の `<w:docGrid w:type="lines" .../>` を
`w:type="default"` にしてセクション単位でグリッドを無効化する。
snapToGrid だけで直らないときの二段目の手。

lineRule を自動で書き換えない理由:
  行間の指定は `auto`（フォントに対する倍率）と `exact`（固定値）で意味が違う。
  Yu Gothic は行高が大きく、`auto` のままだと行間が想定より広がってページから
  あふれることがある。対処は `exact` の固定値だが、**値の決め方は文書ごとに違う**ため、
  後処理で一律に変えると今度は文字が切れる。生成時に指定するのが正しい（docx-layout.md 参照）。
"""
import sys, os, re, shutil, zipfile, argparse, tempfile

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
SNAP_OFF = '<w:snapToGrid w:val="0"/>'


def read_parts(path):
    with zipfile.ZipFile(path) as z:
        return {n: z.read(n) for n in z.namelist()}


def write_parts(path, parts, order):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for n in order:
            z.writestr(n, parts[n])


# ---- 1. styles.xml の docDefaults に snapToGrid=0 を入れる --------------------
def patch_styles(xml):
    """全段落の既定として snapToGrid を切る。ここ1箇所で文書全体に効く。"""
    s = xml.decode("utf-8")
    if "w:pPrDefault" not in s:
        # pPrDefault ごと作る
        m = re.search(r'(<w:docDefaults[^>]*>)', s)
        if not m:
            return xml, False
        ins = f'<w:pPrDefault><w:pPr>{SNAP_OFF}</w:pPr></w:pPrDefault>'
        s = s[:m.end()] + ins + s[m.end():]
        return s.encode("utf-8"), True

    # 既存の pPrDefault > pPr に差し込む
    m = re.search(r'<w:pPrDefault>\s*<w:pPr\b([^>]*)(/?)>', s)
    if not m:
        return xml, False
    if m.group(2) == "/":  # <w:pPr/> の自己終了
        s = s[:m.start()] + f'<w:pPrDefault><w:pPr>{SNAP_OFF}</w:pPr>' + s[m.end():]
        return s.encode("utf-8"), True
    head_end = m.end()
    body = s[head_end:]
    if body.lstrip().startswith("<w:snapToGrid"):
        # 既にある → 値を 0 に矯正
        s2 = re.sub(r'<w:snapToGrid[^/>]*/?>', SNAP_OFF, s, count=1)
        return s2.encode("utf-8"), s2 != s
    s = s[:head_end] + SNAP_OFF + body
    return s.encode("utf-8"), True


# ---- 2. document.xml の明示的な snapToGrid=1 を落とす -------------------------
ON_VALS = ('w:val="1"', 'w:val="true"', 'w:val="on"')


def patch_document(xml, docgrid_off=False):
    s = xml.decode("utf-8")
    n_snap = 0

    def _snap(m):
        nonlocal n_snap
        tag = m.group(0)
        if any(v in tag for v in ON_VALS) or re.match(r'<w:snapToGrid\s*/?>$', tag):
            n_snap += 1
            return SNAP_OFF
        return tag

    s = re.sub(r'<w:snapToGrid\b[^>]*/?>', _snap, s)

    n_grid = 0
    if docgrid_off:
        def _grid(m):
            nonlocal n_grid
            tag = m.group(0)
            if 'w:type="default"' in tag:
                return tag
            n_grid += 1
            return re.sub(r'w:type="[^"]*"', 'w:type="default"', tag)
        s = re.sub(r'<w:docGrid\b[^>]*/?>', _grid, s)

    return s.encode("utf-8"), n_snap, n_grid


# ---- 3. 診断 ------------------------------------------------------------------
def diagnose(parts):
    doc = parts.get("word/document.xml", b"").decode("utf-8", "ignore")
    sty = parts.get("word/styles.xml", b"").decode("utf-8", "ignore")
    report = []

    grids = re.findall(r'<w:docGrid\b[^>]*>', doc)
    on_grid = [g for g in grids if 'w:type="default"' not in g]
    if on_grid:
        report.append(f"行グリッドが有効なセクション: {len(on_grid)} 箇所 → 行間が切り上げられます")

    snap_on = [t for t in re.findall(r'<w:snapToGrid\b[^>]*>', doc)
               if any(v in t for v in ON_VALS)]
    if snap_on:
        report.append(f"snapToGrid=1 の段落指定: {len(snap_on)} 箇所")

    if "w:pPrDefault" not in sty or "snapToGrid" not in sty:
        report.append("styles.xml の既定に snapToGrid=0 がありません（全段落がグリッドに吸着します）")

    auto = re.findall(r'<w:spacing\b[^>]*w:lineRule="auto"[^>]*>', doc)
    if auto:
        report.append(
            f'lineRule="auto" の行間指定: {len(auto)} 箇所 → '
            "Yu Gothic 等では行高が想定より広がることがあります"
            "（自動修正しません。生成側で exact を指定してください）")

    fonts = set(re.findall(r'w:(?:ascii|eastAsia)="([^"]*Gothic[^"]*|[^"]*ゴシック[^"]*)"', doc))
    if any("Yu" in f or "游" in f for f in fonts):
        report.append(f"游ゴシック系フォントを使用: {sorted(fonts)} → 行高に注意")

    return report


def main():
    ap = argparse.ArgumentParser(description="Word 日本語文書の行グリッド起因の崩れを修正する")
    ap.add_argument("path", help="対象の .docx")
    ap.add_argument("-o", "--output", help="出力先（省略時は上書き）")
    ap.add_argument("--check", action="store_true", help="診断のみ。書き換えない")
    ap.add_argument("--docgrid-off", action="store_true",
                    help="sectPr の docGrid を type=default にしてグリッド自体を無効化する")
    a = ap.parse_args()

    if not os.path.isfile(a.path):
        print(f"見つかりません: {a.path}")
        return 2
    if not a.path.lower().endswith(".docx"):
        print("対象は .docx のみです。")
        return 2

    parts = read_parts(a.path)
    order = list(parts.keys())

    print(f"■ {a.path}")
    for line in diagnose(parts) or ["問題は見つかりませんでした。"]:
        print(f"  - {line}")

    if a.check:
        return 0

    if "word/styles.xml" in parts:
        parts["word/styles.xml"], changed_sty = patch_styles(parts["word/styles.xml"])
    else:
        changed_sty = False

    parts["word/document.xml"], n_snap, n_grid = patch_document(
        parts["word/document.xml"], docgrid_off=a.docgrid_off)

    out = a.output or a.path
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
    write_parts(tmp, parts, order)
    shutil.move(tmp, out)

    print("\n修正:")
    print(f"  - styles.xml の既定に snapToGrid=0 を設定: {'済' if changed_sty else '変更なし'}")
    print(f"  - 段落の snapToGrid を 0 に矯正: {n_snap} 箇所")
    if a.docgrid_off:
        print(f"  - docGrid を type=default に変更: {n_grid} 箇所")
    print(f"  → {out}")
    print("\n※ PDF に変換して目視で確認してください（soffice → pdftoppm）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
