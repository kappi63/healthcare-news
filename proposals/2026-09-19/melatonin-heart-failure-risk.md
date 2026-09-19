# 追加提案: 長期メラトニン服用と心不全リスク  （2026-09-19 / 記者AI）

## 1. 関連性
クライアントが睡眠補助目的でメラトニンサプリを使用するケースは多い。
`supplement-criteria.md` の「提案しない・慎重にすべきライン」に現時点でメラトニンへの言及がなく、
長期使用時の心血管系リスクに関するフラグが欠けている。
触れるマーカー/パターン: サプリ評価（問診[18]）・心臓関連主訴（症状逆引き）。

## 2. 新規性（重複チェック結果）
- `terms.json`・`patterns.md`・`bibliography.md`・`supplement-criteria.md` のいずれにもメラトニンの記載なし。
- `interactions.md` にもメラトニンの相互作用は未収録。
- 新規追加に相当。

## 3. エビデンスの強さ
情報源:
- 主要研究: Abstract 4371606, Circulation 2025 (American Heart Association Scientific Sessions 2025)
  — TriNetX Global Research Networkを用いた後ろ向きコホート、不眠症診断のある成人130,000人超、
    傾向スコアマッチング後 メラトニン群65,414人 vs 対照65,414人、追跡5年
  — ハザード比 HR 1.89（心不全発症）、HR 2.09（全死因死亡）
  — 絶対リスク差: 1.9%（HF発症: 5% vs 3%）
- 機序論文（査読済）: PMC13323919「Melatonin supplementation, hyperprolactinemia, and incident heart failure: A proposed prolactin-mediated pathway for cardiovascular risk」2026年
  — メラトニン→高プロラクチン血症→心不全という経路を仮説提示

タグ: **中程度**
一言評価: 大規模コホート（n=13万）だが未査読の学会抄録（AHA 2025）が主要出典であり、
フルペーパー未公表。機序論文は査読済みだが仮説段階。観察研究で因果は未証明。
フルペーパー公表後に「確立寄り」への引き上げを検討。

## 4. 実行可能性
カウンセリング助言に落ちる形:
「現在サプリ一覧を確認する場面（問診[18]）でメラトニン長期使用が判明した場合、
 心血管リスクの文脈で主治医相談を促す一文を追加する」
実装方法は supplement-criteria.md の「提案しない・慎重にすべきライン」へ注記として追加。

## 5. 反映先（差分案）
対象ファイル: `references/supplement-criteria.md`（「提案しない・慎重にすべきライン」セクション末尾）

差分案（追記案）:
```
- **メラトニンの長期使用（1年以上）**: 不眠症患者を対象とした大規模コホート（n=13万、AHA 2025抄録）で
  心不全リスク上昇（HR 1.89）が報告されている。現時点で未査読（フルペーパー未公表）だが、
  クライアントがメラトニンを1年以上継続使用している場合は、主治医への確認を勧め、
  長期継続の必要性を問い直すきっかけとする。
  ※理想値(optimal/reference)の変更ではなく、問診評価時の注意事項として収録。
```

※ 理想値（optimal / reference）の変更は含まない。

## 6. 安全・医療フラグ
心不全は重篤な疾患のため、リスク増加を示すデータがある場合は医師案件フラグを要する。
特に既往に心疾患・高血圧・糖尿病を持つクライアントで長期使用中の場合は優先度高。
妊娠中のメラトニン使用は既存の「医師指導優先」ルールで対応済み。

## 7. 出典（bibliography 追加行）
| S037 | Abstract 4371606: Effect of Long-term Melatonin Supplementation on Incidence of Heart Failure in Patients with Insomnia. Circulation. 2025;152(Suppl_3) (AHA Scientific Sessions 2025) / PMC13323919 Melatonin supplementation, hyperprolactinemia, and incident heart failure (2026) | メラトニン長期使用と心不全リスク | supplement-criteria.md | 中程度（大規模コホート・抄録段階） | 2026-09-19 |

URL/DOI:
- https://www.ahajournals.org/doi/10.1161/circ.152.suppl_3.4371606
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13323919/

## 8. 回帰テスト
影響しうる case: なし（現行テストで直接関係するケースはない）
確認内容: supplement-criteria.md 変更後も既存のサプリ提案ロジック（ビタミンD・鉄・亜鉛等）が
正常に動作することを確認。

## 推奨
**保留** — 理由: フルペーパー未公表の学会抄録が主要出典。絶対リスク差（1.9%）は
相対リスク（90%増）より小さく、観察研究で交絡が残る。フルペーパー公表後に
エビデンスタグを再評価し採用を検討する。今は「参考情報として記録」に留める。
