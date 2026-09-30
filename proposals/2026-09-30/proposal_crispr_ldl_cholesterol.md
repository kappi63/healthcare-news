# 追加提案: CRISPR遺伝子編集療法CTX310によるLDL・中性脂肪の長期低下  （2026-09-30 / 記者AI）

## 1. 関連性
脂質異常症（特に家族性高コレステロール血症）に対し、CRISPR-Cas9によるANGPTL3遺伝子編集療法
（CTX310）が1回投与でLDL 53%・中性脂肪 48%を12カ月低下させた（NEJM掲載、ESC 2026発表）。
触れるマーカー: LDLコレステロール、中性脂肪（TG）、パターンI1（脂質バランス不良）。
家族性高コレステロール血症（FH）の説明文脈に「遺伝子療法の新展開（医師案件）」として
言及できる可能性がある。

## 2. 新規性（重複チェック結果）
- `terms.json`: "CRISPR" "ANGPTL3" "CTX310" のエントリなし → 新規
- `patterns.md` I1: 「家族性高コレステロール血症は医師案件」として記載済み。CRISPR療法の言及なし。
  → 既存記載に**医療オプションの補足**として追加できる可能性（既存更新の可能性あり）
- `bibliography.md`: S024（脂質・動脈硬化リスクの一般知見）は既存。CRISPR療法は新規。
  → S039として仮付番（S037=ウロリチンA提案中、S038=コーヒー提案中のため）

## 3. エビデンスの強さ
情報源: 第I相臨床試験（first-in-human、n=15）、*New England Journal of Medicine* 掲載、ESC 2026発表
タグ: **疾患関連_要医師**
一言評価: 最高権威誌（NEJM）掲載・一流の一次情報だが、Phase I・小規模（n=15）・
対象は「難治性脂質異常症（FH等）」に限定される。栄養的介入ではなく遺伝子工学的医療行為。
精密栄養スキルの主対象（食事・生活習慣の改善アドバイス）の範囲外。

## 4. 実行可能性
CRISPR遺伝子編集は医師による医療施設での処置であり、食事・栄養指導に落としこめない。
「家族性高コレステロール血症の場合は医師へ」という既存の医師案件フラグを超える栄養的示唆はない。
**実行可能性: なし**（栄養カウンセリング助言に落ちない）。

## 5. 反映先（差分案）
対象ファイル: なし（スキル本体への差分反映は不可）

参考情報として patterns.md I1の「家族性高コレステロール血症（若年でのLDL著明高値・家族歴・
腱黄色腫）は医師案件」の注記に「遺伝子療法など新たな医療オプションが登場しつつある」を
1行加える案もありうるが、Phase I段階では医療情報としての記載も時期尚早と判断。
→ bibliography（S039）への記録のみ推奨。差分案なし。

※ 理想値（optimal/reference）の変更は含まない。

## 6. 安全・医療フラグ
完全に医師案件。FH疑いの患者への栄養指導場面でこの情報を持ち出す場合も、
「医師に相談してください」の一言に収める。遺伝子療法を推薦・説明する行為はスキルの範囲外。

## 7. 出典（bibliography 追加行）
| S039 | Raal FJ, et al. CRISPR gene-editing therapy (CTX310) targeting ANGPTL3 safely lowered LDL-C 52.5% and TG 47.8% at 12 months: Phase I trial. *New England Journal of Medicine*. 2026. doi:TBD（Cleveland Clinic / ESC 2026発表）| CRISPR-Cas9遺伝子編集によるLDL・TG長期低下（家族性高コレステロール血症） | 記録のみ（patterns.md I1 参考） | 疾患関連_要医師 | 2026-09-30 |
URL: https://newsroom.clevelandclinic.org/2026/08/28/cleveland-clinic-first-in-human-trial-of-crispr-gene-editing-therapy-shown-to-safely-and-continuously-lower-cholesterol-and-triglycerides-after-one-year

## 8. 回帰テスト
影響しうる case: なし（差分なしのため）
確認内容: 差分なし。記録のみのためテスト対象外。

## 推奨
**見送り** — 理由: 遺伝子工学的医療処置であり、栄養カウンセリング助言に落としこめない。
bibliography S039として参照記録のみ。スキル本体への差分反映なし。
