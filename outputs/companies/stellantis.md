# Stellantis — IVI Agentic AI 実装ファクトブック

**Tier：** T1
**分類：** P3-T（C Orch外部依存・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026 出荷 1.4M 台 +12% YoY、Filosa CEO 「年次実行」言明、Investor Day 2026.5.21予定。L3 ADAS プログラム中止（コスト・需要懸念）、Jeep/Ram/Peugeot/Fiat 4 core brands 集中投資へ
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Stellantis Q1 2026 公式（2026.4）+ CBT News（L3 中止）

---

## 1. エグゼクティブサマリ

Stellantis は Mistral AI（仏）一社依存で全社 AI 戦略を組む P3-T 単一型。FY2025 通期 5.2M 台、Net revenue €153.5B（-2%）、**Net loss €22.3B**（戦略転換 25.4B チャージ起因）。Q1 2026 で出荷1.4M 台 +12% YoY と回復軌道、新CEO Antonio Filosa が「年次実行」と宣言。Investor Day 2026.5.21 で全戦略開示予定。**L3 自動運転プログラム中止**（コスト・需要懸念、2026 Q1）でADAS 戦略縮小。**4 core brands（Jeep/Ram/Peugeot/Fiat）集中投資**にシフト。STLA Brain + STLA SmartCockpit は spring 2026 量産（Peugeot e-3008 / Lancia Gamma）継続。Honda にとっては「P3 路線がもたらす資本効率と引き換えのコントロール喪失」を可視化する反面教材であり、L3 中止は「BEV/SDV戦略 fall-back」の前例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Peugeot e-3008/Lancia Gamma（STLA Medium）[一次] |
| 量産時期 | STLA Brain + SmartCockpit 2026春 [一次] |
| 対象国 | 欧州中心（Lancia は伊）[一次] |
| 旗艦年産 | e-3008 / Gamma 個別量産規模 [未特定] |
| AI Agent搭載総台数 | STLA Medium 全車（年200K+）[推論] |
| FM Level | A（API利用型、Mistral 単一）|
| 主要採用FM | Mistral AI（Le Chat Enterprise 系）[一次] |
| 採用Orchestrator | STLA Brain + STLA SmartCockpit 自前 [一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆〜高級（Peugeot/Jeep/Lancia 全社）[一次]
- 旗艦モデルの市場定位：STLA Medium platform を起点に Peugeot e-3008、Lancia Gamma で量産投入
- 量産時期と地域戦略：欧州中心、北米回復（H2 2025 +11%）、中国は限定 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 表層対話 + 取扱説明書代替（リアルタイム音声マニュアル）[一次] |
| 体験の深さ | 表層対話 → Tool Use（ローンチ時マニュアル QA 主体）[一次] |
| 個別最適化度 | [未特定]（Mistral カスタマイズ未公開）|

UXシナリオ要約：
警告灯の意味を音声で質問すると取扱説明書相当の回答が即時返る [一次]。複合タスク・自律実行は2026春時点で未確認。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-T、Multi-Agent 空欄
- 分類根拠：Orchestrator は STLA Brain 自前だが、FM・主要 Tool・Innovation Lab を Mistral 共同開発に依存 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用型）
- 6要素配分：
  - アーキテクチャ：外部（Mistral）
  - ウェイト：API
  - 事前学習データ：外部依存
  - Fine-tuningデータ：[未特定]（Mistral カスタマイズ範囲非公開）
  - 学習インフラ：Microsoft Azure（5年契約）[推論]
  - 推論ランタイム：外部SDK + STLA Brain 一部

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Mistral AI（Le Chat Enterprise 系）[一次] |
| 採用Orchestrator | STLA Brain + STLA SmartCockpit 自前 [一次] |
| 採用ミドルウェア（IVI OS）| STLA SmartCockpit（STLA Brain上層）[一次] |
| 採用チップ（SoC）| Qualcomm（STLA Brain ベース）[推論] |
| R&D投資規模（AI関連年額）| Mistral 拡張提携（額非公開）+ Microsoft 5年契約 [推論] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Mistral AI（仏・全社契約、Innovation Lab共同開発）[一次] |
| Orchestrator提供 | 自社（STLA Brain）+ Mistral 共同開発 [一次] |
| Chip提供 | Qualcomm + NVIDIA（個別車種別）[推論] |
| データ・地図提供 | TomTom / HERE [推論] |
| ADAS提供 | Wayve（Series D 出資、量産時期未公開）+ STLA AutoDrive 自前 [一次] |
| 親グループ（P4のみ）| Stellantis NV（独立、PSA + FCA 統合体）[一次] |

---

## 5. 将来：どこへ向かうか

### 5.1 内製意志（戦略宣言ファクト）
- 公式宣言：Mistral AI 拡張提携（2025.10）"全社AI 採用加速"、Innovation Lab 共同開発 18ヶ月 [一次]
- 投資規模：FY2025 通期 5.2M台 / 売上 €153.5B / **Net loss €22.3B**（戦略転換の25.4B チャージ起因）[一次]
- 移行ロードマップ：STLA Brain + STLA SmartCockpit = spring 2026（Peugeot e-3008 / Lancia Gamma）[一次]、Wayve（Series D 出資、量産時期未公開）+ Foxconn（Mobile Drive JV）+ Microsoft 5年AIディール [推論]
- 動機：コスト最小化（外部FM一社 = Mistral）+ 欧州主権（仏Mistral 選好）+ 財務危機ゆえの選択肢縮小 [推論]

### 5.2 2027/2030 戦略パターン遷移予測
- 現在：P3-T（C 外部単一依存 = Mistral）
- 2027：P3-T or P3-E（Mistral 拡張）+ Wayve ADAS（確度：低-中）
- 2030：P3-E or P2-T 移行（財務回復次第）（確度：低-中）
- 分岐条件：Net loss 解消 + Wayve 出資効果 = 一部内製化 / 失敗継続 = 完全依存P3-T 固定

### 5.3 in-Car 5観点 実装ステータス

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 2026予定（STLA Brain + SmartCockpit, spring 2026, Peugeot e-3008/Lancia Gamma）[一次] |
| a-2 ナビ・ルート | 2026予定（Mistral 連携、ナビ統合詳細[未特定]）|
| a-3 コックピット制御 | 部分実装（STLA Brain で OTA + 制御）[一次] |
| a-4 乗員ケア | [未特定] |
| a-5 コマース | [未特定] |

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- P3-T 単一型（外部FM一社依存）を選んだ場合、財務制約下では選択肢の柔軟性を失う。Honda が Gemini 単一に陥るリスクへの警告
- 取扱説明書代替（リアルタイム音声マニュアル）は2026春の最初の量産機能として現実的なターゲット。Honda 0 Series でも同等機能の優先実装余地あり
- Wayve（Series D）出資で ADAS 二段構え化。Honda の Helm.ai + Momenta 二段構えと類似構造

### 6.2 警鐘 or 注意点
- Net loss €22.3B の財務危機が AI 戦略の幅を狭める。Honda が同様の財務逆風に遭遇すれば P3-T 路線を強いられる可能性
- Mistral 一社依存により、Mistral の競争力低下時に代替手段がない。Multi-Agent への移行コストが高くつく構造

### 6.3 Honda の現在地との差分
Honda の P2-T（ASIMO OS + Gemini）と Stellantis の P3-T は近似する見え方だが、Honda は Helm.ai + AGL SoDeV で Orchestration 自前路線を選択しており、Stellantis よりも Mercedes 寄り。Stellantis 型への退行を回避する戦略規律が必須。

---

## 7. [未特定] 残課題

- Stellantis STLA SmartCockpit Mistral 機能の Tool Use 数（理由：「リアルタイム取扱説明書」のみ確認、複合タスク仕様未公開）
- Stellantis 通期販売台数 公式数字（理由：Q1〜Q4 推定合算 5.2-5.4M、公式の通期確定数字 [未特定]）
- Mistral カスタマイズ・Fine-tune 範囲（理由：Innovation Lab 内部仕様非公開）
- Wayve ADAS 量産投入時期（理由：Series D 出資のみ確認、量産年未公表）
- 2026.5.21 Investor Day 開示予定の中期計画詳細
- L3 中止後の ADAS 構成（Wayve 投資の処遇含む）

## 8. 2026 Q1-Q2 追加ファクト

- **2026 Q1 出荷 1.4M台 +12% YoY**（米国 +4%）= 回復軌道。CEO Filosa 「2026 は実行の年」[一次]
- **L3 自動運転プログラム中止**（2026 Q1、コスト・需要懸念）[二次]
- 投資集中：Jeep/Ram/Peugeot/Fiat の 4 core brands に future investment 集約 [二次]
- 2026 通期見通し：Net revenue 中一桁 % 成長、Adjusted operating margin 低一桁 % [一次]
- 2026.5.21 Investor Day で Filosa 中期計画を開示予定 [一次]
- $4.1B CATL JV（スペイン電池）、Factorial Energy（固体電池）、Mistral AI（自動運転）の三大提携継続 [一次]

## 出典（2026 Q1追加）

- [Stellantis 公式 — Q1 2026 Estimated Consolidated Shipments](https://www.stellantis.com/en/news/press-releases/2026/april/stellantis-reports-q1-2026-estimated-consolidated-shipments-of-1-4-million-units-12-percent-y-o-y) [一次]
- [Reuters / BNN — Stellantis to focus funding on core car brands](https://www.bnnbloomberg.ca/business/2026/04/24/stellantis-to-focus-funding-on-core-car-brands-as-ceo-drives-turnaround-reuters-sources-say/) [二次]
- [CBT News — Stellantis halts Level 3 driver-assistance program](https://www.cbtnews.com/stellantis-halts-level-3-driver-assistance-program-amid-cost-and-demand-concerns/) [二次]


## 直近アップデート
- 2026-05-11: LeapmotorとのOpel EV・スペイン工場移管でパートナーシップ深化。 ([出典](https://cnevpost.com/2026/05/08/stellantis-deepens-leapmotor-tie-up-opel-ev-spanish-plant-transfer/))
