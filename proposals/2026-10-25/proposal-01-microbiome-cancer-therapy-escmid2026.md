# 追加提案: 腸内マイクロバイオームとがん治療効果（ESCMID 2026）  （2026-10-25 / 記者AI）

## 1. 関連性
ESCMID 2026学会で発表された「腸内マイクロバイオームのがん治療応答への影響」の知見。
触れるパターン・マーカー: patterns.md(G1 低多様性ディスバイオシス / G2 酪酸産生菌低下 / G3 有用菌低下)。
S006（腸内細菌叢の一般知見）・S026（PPGR個人差と腸内細菌）・S030（オリーブオイルと腸内細菌）の参照引用先として機能しうる。
腸内フローラ改善の目的に「免疫機能・治療応答への寄与」という新たな文脈が加わることで、カウンセリング上の根拠を強化できる。

## 2. 新規性（重複チェック結果）
- S006: 一般的な腸内細菌多様性・SCFA・ディスバイオシスの知見 → 既出（上位概念）
- S026: 食後血糖と腸内細菌（P. copri）→ 食事応答の文脈で既出
- S030: オリーブオイルと腸内多様性・認知機能 → 異なる疾患アウトカム
- 今回の知見「腸内マイクロバイオームがん治療応答修飾（FMT臨床試験）」は bibliography に未収録 → **新規**
- gut-flora.md・G1〜G3 のパターン本文にがん治療文脈への言及はない → **新規追記候補**

## 3. エビデンスの強さ
情報源: ESCMID 2026 学会発表（会議録レビュー）+ Phase I/II 臨床試験（腎臓がん・肺がん・メラノーマ）
タグ: **中程度**（疾患関連_要医師）
一言評価: Phase I/II レベルの臨床試験複数で腸内マイクロバイオーム介入と治療応答の関連が示されているが、大規模RCTによる確立には至っていない。ESCMID 学会は権威ある感染症学会（一次情報として信頼性あり）。Phase III 試験が開始されており将来の確立が見込まれる段階。

## 4. 実行可能性
カウンセリングへの落とし込みの可否: **限定的・枠組み追記のみ**
- FMT（便微生物移植）は医療行為であり、栄養カウンセリングの範囲外。
- ただし「なぜ腸内フローラを食事・サプリで整えることが重要か」の根拠として、
  免疫治療・抗がん剤の応答に腸内環境が影響するという点を文脈注記として追記することは実行可能。
- 具体的助言: 「多様な植物性食品・発酵食品・食物繊維による腸内多様性サポート」は既存 G1〜G3 に沿う。
- 新規の具体的助言（プロバイオティクス種・量）は指定する根拠がまだない。

## 5. 反映先（差分案）
対象ファイル: `functional-tests/gut-flora.md` G1 補足注記 / `references/bibliography.md` 追記

差分案（bibliography 追記行）:
```
| S037 | Microbiome modulation as a determinant of cancer therapy response. EMJ Reviews (ESCMID 2026 Congress Highlights). emjreviews.com/…/escmid-2026-j10126/ ／ Davar D, et al. Science. 2021;371(6529):595-602（Phase 1 FMT + pembrolizumab、メラノーマ）/ Baruch EN, et al. Science. 2021;371(6529):602-609（同、転移性メラノーマ） | 腸内マイクロバイオームの組成が免疫チェックポイント阻害薬・抗がん治療の応答を修飾。FMTが臨床試験フェーズへ（Phase I/II 完了、Phase III 開始）。栄養カウンセリングで腸内環境改善を推奨する際の文脈強化根拠 | functional-tests/gut-flora.md / patterns.md(G1) | 中程度（疾患関連_要医師） | 2026-10 |
```

差分案（gut-flora.md / G1 への注記追加）:
```
> **〔参考〕** 腸内多様性の低下（ディスバイオシス）は、近年の臨床試験（Phase I/II）で免疫チェックポイント阻害薬など抗がん治療の応答率とも関連することが示されている（S037）。FMT（便微生物移植）は医療行為であり栄養カウンセリングの範囲外。食事・食物繊維介入による腸内多様性サポートの意義を説明する文脈として参照してよい。
```

※ 理想値（optimal/reference）は変更しない。

## 6. 安全・医療フラグ
- FMT は感染リスクを伴う侵襲的医療行為 → **医師案件**。提案ではFMT推奨を行わない。
- 免疫チェックポイント阻害薬の使用者は免疫状態が特殊 → 食事・サプリ介入でも医師確認を優先。
- 過剰なプロバイオティクス使用による菌血症リスクの懸念は既存 output-checklist.md が対応。

## 7. 出典（bibliography 追加行）
| S037 | ESCMID 2026 Congress Review: Microbiome Modulation as a Determinant of Cancer Therapy Response. EMJ Reviews. 2026. | 腸内マイクロバイオームとがん治療応答 | gut-flora.md / patterns.md(G1) | 中程度（疾患関連_要医師） | 2026-10 |
URL: https://www.emjreviews.com/microbiology-infectious-diseases/congress-review/microbiome-modulation-as-a-determinant-of-cancer-therapy-response-highlights-from-escmid-2026-j10126/

補完一次文献:
- Davar D, et al. Fecal microbiota transplant overcomes resistance to anti–PD-1 therapy in melanoma patients. Science. 2021;371(6529):595-602. DOI: 10.1126/science.abf3363
- Baruch EN, et al. Fecal microbiota transplant promotes response in immunotherapy-refractory melanoma patients. Science. 2021;371(6529):602-609. DOI: 10.1126/science.abb5920

## 8. 回帰テスト
影響しうる case: G1〜G3 関連ケース（腸内フローラ検査があるプロファイル）
確認内容: gut-flora.md の G1 に注記を追加した場合、既存の腸内フローラ解析テストケース（低多様性ディスバイオシス型の提案出力）が変わらないことを確認する。新規の助言内容は追加されないため回帰影響は軽微と予想。

## 推奨
**保留** — 理由: Phase I/II 臨床試験ではマイクロバイオームとがん治療応答の関連が示されているが、栄養カウンセリングへの具体的助言に落とし込む根拠は限定的。bibliography への参照追加と gut-flora.md への文脈注記は適切だが、Phase III 試験結果（2026〜2027年予定）を確認後に改めて評価することを推奨。出典の一次情報（Science 2021論文）は査読済みで信頼性あり。
