#!/usr/bin/env python3
"""
遺伝子検査の生データから、精選SNP（genetics-snps.json）に該当する遺伝型を抽出する。
使い方: python analyze_genetics.py <genotype_file> [snps_json]
入力: 23andMe/AncestryDNA形式（rsid  chrom  pos  genotype のTSV、# はコメント）や、
      「rsid, genotype」列を含むCSV/TSVに対応。
出力: 該当SNPの遺伝型と要点をJSONで標準出力。

重要: 遺伝は体質・確率であり診断ではない。疾患関連変異は医師案件。
      詳しい解釈・安全上の注意は references/functional-tests/genetics.md を参照。
"""
import sys, json, os, re

def load_snps(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def parse_genotypes(path):
    """rsid -> genotype の辞書を返す。TSV/CSV/23andMe形式を緩く判定。"""
    geno = {}
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = re.split(r"[\t,;]+", line)
            if len(parts) < 2:
                parts = line.split()
            # rsidらしきトークンを探す
            rs = next((p for p in parts if p.lower().startswith("rs")), None)
            if not rs:
                continue
            # 遺伝型らしきトークン（A/C/G/T/D/I の1〜2文字、または A/A 形式）
            gt = None
            for p in parts[parts.index(rs)+1:]:
                q = p.replace("/", "").replace("|", "").upper()
                if q and all(c in "ACGTDI-" for c in q) and 1 <= len(q) <= 2:
                    gt = q; break
            if gt:
                geno[rs.lower()] = gt
    return geno

def main():
    if len(sys.argv) < 2:
        print("usage: analyze_genetics.py <genotype_file> [snps_json]"); sys.exit(1)
    gfile = sys.argv[1]
    here = os.path.dirname(os.path.abspath(__file__))
    snps_json = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(here, "..", "references", "functional-tests", "genetics-snps.json")
    snps_json = os.path.abspath(snps_json)

    data = load_snps(snps_json)
    geno = parse_genotypes(gfile)

    results = []
    for s in data["snps"]:
        rsids = re.findall(r"rs\d+", s["rsid"])  # 複合表記から個々のrsIDを抽出
        found = {rid: geno[rid.lower()] for rid in rsids if rid.lower() in geno}
        results.append({
            "gene": s["gene"], "rsid": s["rsid"],
            "検出": found if found else "データになし",
            "affects": s["affects"], "effect": s["effect"],
            "nutrition": s["nutrition"], "related_patterns": s.get("related_patterns", []),
            "evidence": s["evidence"], "caution": s.get("caution", "")
        })

    matched = [r for r in results if r["検出"] != "データになし"]
    out = {
        "検出できたSNP数": len(matched),
        "対象SNP総数": len(results),
        "結果": results,
        "免責": "遺伝は体質・確率であり診断ではない。疾患関連変異(APOE ε4・HFE等)や飲酒×ALDH2の"
                "発がんリスク等は医師・遺伝カウンセリング案件。消費者検査の生データは誤りを含みうる。"
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
