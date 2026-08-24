# 追加提案: ペパーミントオイルと血圧低下  （2026-08-24 / 記者AI）

## 1. 関連性
軽度高血圧（前高血圧〜ステージ1）へのペパーミントオイル補充が収縮期血圧を有意に低下させた RCT。
スキルが扱うマーカー・パターンとの関係：
- **血圧管理**: 現行スキルに血圧関連の食事・サプリ助言はあるが（patterns.md の C2/I1 周辺）、ペパーミントオイルの具体的言及はない。
- **植物性補助食品**: 食事助言の選択肢として植物エキス（オリーブ油等）は記載あり。ペパーミント（メントール系）は未記載。
- **サプリ提案の判断基準（supplement-criteria.md）**: 不足補充でなく機能的効果のサプリ。

## 2. 新規性（重複チェック結果）
- `references/patterns.md`: ペパーミントオイル・メントール系の記述なし（**新規**）。
- `references/supplement-criteria.md`: 植物エキス系の血圧補助は未記載（**新規**）。
- `references/bibliography.md`: Sinclair 2026 *PLOS One* 未収録（**新規**）。

## 3. エビデンスの強さ
情報源: Sinclair DJ et al. "Effects of peppermint (*Mentha × piperita* L.) oil on cardiometabolic outcomes in patients with pre- and stage 1 hypertension: A placebo randomized controlled trial." *PLOS One*. 2026. DOI: 10.1371/journal.pone.0344538
タグ: **仮説**（保留）
一言評価: 並行無作為化プラセボ対照 RCT という設計は適切だが、**n=40、期間20日の小規模短期試験**であり、一般化には十分でない。単一施設・短期・少数例で「確立」には達しない。PLOS One は査読誌だが，n が小さく追試が必要。

## 4. 実行可能性
カウンセリング助言への落とし方：
- 軽度高血圧（前高血圧〜ステージ1）クライアントへの非薬物アプローチの選択肢として「ペパーミントオイル100μL/日（2回分割投与）」の話題提供は可能。
- ただし **証拠が小規模1試験のみ**のため、「試験的に注目されている」「追試が待たれる」という情報提供にとどめ、強い推奨はしない。
- メントール主成分が血管拡張に関与する機序は先行研究で示唆あり（交感神経抑制・カルシウム拮抗様作用）。
- 薬の変更・中止の提案は行わない（禁止事項）。

## 5. 反映先（差分案）
対象ファイル: `precision-nutrition-analysis/references/supplement-criteria.md`（または patterns.md 関連箇所）
差分案（参照コメントとして追記案）:
```
【仮説段階・追試待ち】ペパーミントオイル（100μL/日，20日）が軽度高血圧患者の
収縮期血圧を-8.5 mmHg 低下させた小規模 RCT（n=40, *PLOS One* 2026, Sinclair 等）。
エビデンスは限定的だが，非薬物補助アプローチとして言及できる〔仮説／S038〕。
薬の変更や中止を促す文脈では使用しない。
```

※ **理想値（optimal/reference）は変更しない。** 血圧の参照値は据え置き。

## 6. 安全・医療フラグ
- 血圧管理は医師案件。薬物療法中のクライアントへの提案には注意。「薬を変える・やめる」提案禁止。
- ペパーミントオイルの過剰摂取（高用量）には消化器刺激・乳幼児への禁忌などがある点を注記。
- 本試験の対象は前高血圧〜ステージ1のみ（より高いステージへの外挿は不適切）。

## 7. 出典（bibliography 追加行）
| S038 | Sinclair DJ, et al. Effects of peppermint (*Mentha × piperita* L.) oil on cardiometabolic outcomes in patients with pre- and stage 1 hypertension: A placebo RCT. *PLOS One*. 2026. DOI:10.1371/journal.pone.0344538 | 植物性補助食品・血圧 | supplement-criteria.md（または patterns.md） | 仮説（小規模RCT） | 2026-08-24 |
URL: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0344538

## 8. 回帰テスト
影響しうる case: 血圧・循環器リスク関連ケース（I1/I2 パターン）
確認内容: 既存の脂質・血圧パターンの記述が変わらないこと（追記のみのため不変のはず）。追加後、血圧関連ケースでペパーミントオイルが誇大に推奨されないことを確認。

## 推奨
**見送り（現時点）** — 理由: n=40・20日間の単一 RCT では実践助言に落とすには根拠が薄い。血圧関連の確立した介入（減塩・DASH食・カリウム・マグネシウム・運動等）との比較で優先度が低い。追試が出た段階で再検討。禁止表現・薬変更への抵触もないが、過剰期待を招くリスクがあるため慎重対応が適切。
