# 追加提案: 腸内細菌由来グリシン脂質と食物繊維・脂肪肝予防  （2026-11-10 / 記者AI）

## 1. 関連性
腸内マイクロバイオームはすでに `bibliography.md` S006/S026/S030 等で収載されているトピック。
今回の研究は「高食物繊維食 → 腸内細菌がグリシン脂質を産生 → 肝臓・骨格筋のミトコンドリア機能改善・MASLD（代謝関連脂肪肝疾患）予防」という新たなメカニズムを提示する。
本スキルが扱う対象マーカーとして、肝機能（AST/ALT/γ-GTP）および糖代謝・脂質代謝マーカーに関係する可能性があり、食物繊維摂取の推奨根拠として関連性あり。

## 2. 新規性（重複チェック結果）
- `bibliography.md` S006: 腸内細菌叢の一般知見（SCFA・ディスバイオシス）収載済み。グリシン脂質という特定の代謝産物については記載なし。
- `bibliography.md` S026: 食物繊維応答と腸内細菌の個人差収載済み。今回の研究は食物繊維→特定脂質産生→臓器代謝という新規メカニズムを扱う点で新規性あり。
- `patterns.md` / 腸内フローラセクション: 食物繊維・SCFA（短鎖脂肪酸）についての記述は存在すると推定されるが、グリシン脂質・MASLD経路は未収載と判断 → **新規仮説候補**

## 3. エビデンスの強さ
情報源: Phys.org（2026年11月）報道 ← 元研究: University of Missouri（マウス実験）
タグ: **仮説**
一言評価: マウス実験のみであり、ヒト介入研究・RCTは未実施。腸内細菌-グリシン脂質-ミトコンドリア経路はメカニズム研究の段階。現時点での採用は時期尚早。ヒトでの検証が必要。

## 4. 実行可能性
カウンセリング助言として落とせる：**現時点では不可**（マウス実験のみ）。
落とせる内容（仮説レベルの補足情報として）：
- 高食物繊維食と腸内細菌の代謝産物多様性については既存S026等に根拠があり、食物繊維推奨の補足メカニズムとして参考情報程度に言及は可能
- 「グリシン脂質による脂肪肝予防」を直接推奨するのは時期尚早

## 5. 反映先（差分案）
対象ファイル: `references/bibliography.md` への参考文献追記のみ（patterns.md への反映は保留）

差分案:
```
【bibliography.md 参考情報として追記（タグ=仮説）】
| S0XX | University of Missouri (2026). Microbiome-derived glycine lipids improve mitochondrial function in liver and skeletal muscle [mouse study]. *[誌名未確認]* | 高食物繊維食→グリシン脂質→肝臓・筋肉のミトコンドリア機能・MASLD予防（マウス実験） | gut-flora.md 参考情報 | 仮説 | 2026-11-10 |
URL: https://phys.org/news/2026-11-microbiome-reveals-bacterial-lipids-liver.html
（一次論文特定要）
```

※patterns.md への反映は保留。理想値は変更しない。

## 6. 安全・医療フラグ
マウス実験の段階であり、ヒトへの安全性・有効性は未確立。
食物繊維摂取増加自体は一般的に安全だが、炎症性腸疾患等では過剰な食物繊維で症状が悪化する場合あり。

## 7. 出典（bibliography 追加行）
| S0XX | University of Missouri / Phys.org (2026-11). Microbiome research reveals how bacterial lipids influence liver and muscle health in mice. | 腸内細菌グリシン脂質・ミトコンドリア・MASLD（マウス） | gut-flora.md参考情報 | 仮説 | 2026-11-10 |
URL/DOI: https://phys.org/news/2026-11-microbiome-reveals-bacterial-lipids-liver.html
（一次論文のDOI・誌名は別途確認要）

## 8. 回帰テスト
影響しうる case: 腸内フローラ関連ケース（gut-flora.md 参照ケース）
確認内容: 既存の腸内細菌・食物繊維推奨が変化しないこと（今回は参考文献追記のみのため影響は最小）

## 推奨
**保留** — 理由: マウス実験のみで、ヒトへの直接外挿は不可。food fiber / microbiome の既存推奨の補足参考情報として bibliography 追記にとどめる。ヒト臨床試験の結果が出た段階で再評価。
