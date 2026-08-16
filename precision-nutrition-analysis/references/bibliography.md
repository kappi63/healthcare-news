# 参考文献・出典リスト（bibliography）

このスキルの判定・理想値・パターンの根拠を記録する台帳。知見を足すたびにここへ1行追加する。
各判定ルールやパターンは、可能な限りこの表の出典と対応づける。
根拠の強さは【確立】（学会ガイドライン・査読論文・公的機関）／【精密栄養】（精密栄養学・
オーソモレキュラー的な実践知・理想値解釈）で区別する。

| ID | 出典（書名・機関・URL等） | 対象トピック | 反映先 | 根拠 | 追加日 |
|---|---|---|---|---|---|
| S001 | 神宮前統合医療クリニック「血液検査データ理想値まとめ」 | 男女別の理想値 | ideal-ranges.md / terms.json(optimal) | 精密栄養 | 2026-07 |
| S002 | 精密栄養学 用語辞書（GitHub: mhd-apps/precision-nutrition-glossary、terms.json内 sources） | 各マーカーの意味・栄養素・関連 | terms.json | 確立＋精密栄養 | 2026-07 |
| S003 | 実サンプルレポート（施術者作成） | 判定の型・文体 | interpretation.md / report-template.md / patterns.md | 精密栄養 | 2026-07 |
| S004 | 回帰テスト（caseB/C）で発見した実践的補正 | 鉄欠乏の反応性血小板増加・体格に依らないビタミンD確認 | patterns.md(B1,D2) | 精密栄養 | 2026-07 |
| S005 | CGM国際コンセンサス指標（TIR・CV<36%・GMI）＋非糖尿病の目安 | リブレ解析の指標・目標 | functional-tests/libre.md / patterns.md(F1,F2) | 確立＋精密栄養 | 2026-07 |
| S006 | 腸内細菌叢の一般知見（多様性・酪酸/SCFA・ディスバイオシス）※相関・仮説が多い | 腸内フローラ解析 | functional-tests/gut-flora.md / patterns.md(G1-G3) | 研究蓄積＋仮説 | 2026-07 |
| S007 | ニュートリジェネティクスのレビュー（Genes&Nutrition 2025 等）＋エビデンス評価指針(PMC5732517)。実証的な食事応答: CYP1A2/APOE/MTHFR/FTO/TCF7L2/VDR。ALDH2(東アジア)。 | 遺伝子解析 | functional-tests/genetics.md, genetics-snps.json / patterns.md(H1-H4) | SNPにより確立〜仮説 | 2026-07 |
| S009 | Tripkovic L, et al. Am J Clin Nutr. 2012;95(6):1357-64. / Balachandar R, et al. Nutrients. 2021;13(10):3328.（メタ解析2件） | ビタミンD2 vs D3 の効力比較 | patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S010 | Burt LA, et al. JAMA. 2019;322(8):736-745.（3年RCT, 400/4000/10000 IU） | 高用量ビタミンDと骨密度・骨強度 | patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S011 | Wallace RB, et al. Am J Clin Nutr. 2011;94(1):270-7.（WHI 尿路結石） / Jackson RD, et al. NEJM. 2006;354:669-683.（WHI Ca+D 骨折） | Ca＋D併用の結石リスク・骨折予防効果の限界 | patterns.md(D2) / terms.json(25-OHD, カルシウム) | 確立 | 2026-07 |
| S012 | Demay MB, et al. J Clin Endocrinol Metab. 2024;109(8):1907-1947.（Endocrine Society 予防ガイドライン） / Pilz S, et al. Nutrients. 2026;18(9):1472.（批判的吟味） | 補充が推奨される対象群（1-18歳・75歳以上・妊婦・前糖尿病）／2011年版の血中目標値撤廃 | vitamin-d-evidence.md / terms.json(25-OHD) | 確立 | 2026-07 |
| S013 | Manson JE, et al. NEJM. 2019;380:33-44.（VITAL） / Hahn J, et al. BMJ. 2022;376:e066452.（VITAL 自己免疫） / Neale RE, et al. Lancet Diabetes Endocrinol. 2022;10:120-128.（D-Health） / Pittas AG, et al. NEJM. 2019;381:520-530.（D2d） | 大規模RCT: がん罹患・心血管・糖尿病発症は予防せず／自己免疫22%減／月1回大量投与は総死亡を下げない | vitamin-d-evidence.md / patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S014 | Jolliffe DA, et al. Lancet Diabetes Endocrinol. 2025;13(4):307-320.（46試験・64,086人） | 急性呼吸器感染の予防: OR 0.94 (0.88-1.00) で有意差なし。2021年版(OR 0.92)からの**格下げ**。毎日・400-1000 IU・1-15歳のみ有意 | vitamin-d-evidence.md / patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S015 | Zhang X, Niu W. Biosci Rep. 2019;39(11):BSR20190369.（RCT 10件・81,362人） | がん死亡 RR 0.87（有意）／がん罹患 RR 0.99（有意差なし）＝罹患と死亡の区別 | vitamin-d-evidence.md / terms.json(25-OHD) | 確立 | 2026-07 |
| S016 | Cui A, et al. Front Nutr. 2023;10:1070808.（308研究・790万人） | 世界の欠乏有病率（<20ng/mL で約48%）／**冬春の低値有病率は夏秋の約1.7倍**＝季節補正の根拠 | vitamin-d-evidence.md / patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S017 | Yoshimura N, et al. Arch Osteoporos. 2025;20(1):117.（ROAD研究 2005-2015）※訂正あり: 同誌 20:127, doi:10.1007/s11657-025-01608-2 | 日本人一般集団: 平均25(OH)D 23.3→25.1 ng/mL、欠乏 29.5%→21.6%。**改善傾向**であり「深刻化」の根拠には使えない | vitamin-d-evidence.md / patterns.md(D2) / terms.json(25-OHD) | 確立 | 2026-07 |
| S018 | Holick MF. NEJM. 2007;357(3):266-281. | 機序・合成経路・欠乏の定義。**有効性の根拠には用いない**（大規模RCT群に先行する2007年の総説。理想値レンジの立場を代表する文献であり循環参照に注意） | vitamin-d-evidence.md（背景・機序のみ） | 機序は確立／有効性は失効 | 2026-07 |

## 追加時のルール
- 出典が確認できないもの（伝聞・出所不明のまとめサイト等）は採用しない。
- 同じトピックで新旧の知見が食い違う場合は、より新しく質の高い出典を優先し、古い行は「置換」と注記。
- 医療に関わる変更は、反映先の該当ルールに出典IDを添え、人（施術者）のレビュー後にマージ。
| S008 | 栄養エピジェネティクスのレビュー（PMC12841049 2026; Front Nutr 2025; 系統的レビューPMC11284312）。メチル基供与体(葉酸/B12/コリン)・ポリフェノール・酪酸のメチル化への影響。※具体的臨床効果は予備的 | epigenetics.md / patterns.md(H1,B3)・gut-flora.md(G2)と連動 | メカニズム確立＋効果は予備的 | 2026-07 |
| S019 | HbA1cの偽高・偽低（赤血球寿命・鉄欠乏・B12/葉酸・造血動態）と代替指標(GA/1,5-AG/CGM)の一般知見 | HbA1c補正 | hba1c-correction.md / patterns.md(C2)・libre.md | 確立 | 2026-08 |
| S020 | 経時比較の運用設計（判定軸・生理的変動/測定誤差の目安・交絡確認）※臨床検査の一般知見に基づく運用ルール | 再検査フォロー | longitudinal-comparison.md / report-template.md / gamma-output.md | 運用設計＋確立 | 2026-08 |
| S021 | 栄養素・薬剤の相互作用の一般知見（亜鉛×銅、鉄×Ca/PPI、ワルファリン×ビタミンK、メトホルミン×B12、甲状腺薬×鉄/Ca、抗菌薬×ミネラル 等） | 相互作用チェック | interactions.md | 確立 | 2026-08 |
| S022 | 症状と栄養マーカーの対応（鉄欠乏症状・亜鉛欠乏症状・甲状腺症状等の一般知見） | 症状逆引き | symptom-index.md | 確立＋精密栄養 | 2026-08 |
| S023 | ライフステージ別の需要変化（月経による鉄喪失、妊娠前後の葉酸、閉経後の鉄・骨・脂質、高齢のフレイル/低栄養） | ライフステージ修飾 | lifestage.md | 確立 | 2026-08 |
| S024 | 脂質と動脈硬化リスクの一般知見（LDL/HDL/L-H比、家族性高コレステロール血症、甲状腺・更年期による変動、低コレステロールと低栄養） | 脂質パターン | patterns.md(I1,I2) | 確立 | 2026-08 |
| S025 | 骨代謝の一般知見（たんぱく質・ビタミンD・K・Ca・Mg、閉経後/高齢のリスク、ALPの解釈） | 骨代謝パターン | patterns.md(J1) | 確立＋精密栄養 | 2026-08 |
| S026 | 食後血糖応答(PPGR)の個人差と予測モデル（血液・食事・体格・活動・腸内細菌の統合／盲検RCTで個別化食事が食後血糖を有意低下）、食物繊維応答とP. copri（反応者/非反応者） | 食事応答の個人差 | dietary-response.md / libre.md(F1,F2) / gut-flora.md(G2) | 確立寄り＋研究蓄積 | 2026-08 |
| S027 | Hu J, et al. Midlife Vascular Risk Burden and Dementia-Free Survival Years: The ARIC Neurocognitive Study. Neurology Open Access. 2026;DOI:10.1212/WN9.0000000000000152（12,409人・中央値26年追跡） | 中年期の高血圧・糖尿病・喫煙の回避と認知症なし生存期間の延長（約13年）※観察研究・因果は未証明 | patterns.md(C2 長期アウトカム／I1 相互参照) | 中程度（大規模観察） | 2026-08 |
| S028 | Ferreri DM, et al. Front Nutr. 2026;13:1858850（食事パターンが個別栄養素と老化速度の関連を修飾／全体パターンと体重が主要因）／Carreras-Gallo N, et al. Aging. 2025;17:699-725（サプリ介入でDunedinPACE上昇）／Karbacher, et al. MedComm 2026（ビーガン食介入で時計により結論が相反）／García-García I, et al. Front Aging. 2024;5:1417625（系統的レビュー：予備的） | 栄養エピジェネティクスの限界と優先順位（パターン＞個別栄養素、サプリ不支持、時計間の不一致、BMI交絡） | epigenetics.md / output-checklist.md / watchlist.md(T5) | 中程度（限界の知見は比較的堅い） | 2026-08 |
| S029 | サプリ提案の判断基準（運用設計）。不足時の補充効果と充足者への上乗せ効果の乏しさ、過剰リスク（鉄・ビタミンA・高用量D・亜鉛単独長期）に関する一般知見に基づく | サプリ提案の可否 | supplement-criteria.md / output-checklist.md | 確立＋運用設計 | 2026-08 |
| S030 | Ni J, Nishi SK, Babio N, et al. Total and different types of olive oil consumption, gut microbiota, and cognitive function changes in older adults. Microbiome. 2026;14(1):68. doi:10.1186/s40168-025-02306-4（PREDIMED-Plus、656人・2年追跡の**前向きコホート**） | バージンolive oilと腸内細菌多様性・認知機能の関連（精製油では逆傾向／Adlercreutziaが一部媒介）※観察研究・因果は未証明 | functional-tests/gut-flora.md / patterns.md(I2) | 中程度（前向きコホート） | 2026-08 |
| S031 | 時間栄養学の総説（Front Nutr 2026;13:1779033 心代謝と概日タイミング／Front Nutr 2026;13:1872454 TRE／Nutrients 2025;17:2135 エネルギーバランス）。遅い時間帯の食事は食事組成・総エネルギーと独立して食後血糖・インスリン感受性・脂質処理に不利。early TREの有益性。朝食欠食の是非は議論あり | 食べるタイミング | chrononutrition.md | 確立寄り〜中程度 | 2026-08 |
| S032 | 日本食品標準成分表2020年版（八訂）ほうれん草のビタミンC季節差（通年平均35mg vs 冬採り60mg/100g）。※季節による成分値の違いはビタミンC以外ほとんど未分析 | 旬の食材 | seasonal-foods.md | 一部確立・一般化は限定的 | 2026-08 |
