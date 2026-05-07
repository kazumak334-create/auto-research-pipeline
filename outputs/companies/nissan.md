# Nissan — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3-T（Wayve・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ 過去四半世紀最深の財務危機継続。FY2026 自動車営業利益・FCF 黒字目標。**新型車開発期間 50ヶ月→37ヶ月 短縮**。Wayve 採用継続（FY2027 量産）+ Tokyo Robotaxi（Wayve+Uber+Nissan、2026後半）。**Honda統合協議は2025.2に決裂済（Honda側 Nissan を子会社化要求が原因）**
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ ION Analytics + CBT News + Manufacturing Today

---

## 1. エグゼクティブサマリ

Nissan は次世代 ProPILOT を Wayve（英）AI Driver で構築（FY2027 量産）。Wayve+Nissan+Uber で Tokyo Robotaxi パイロット計画（2026年後半、当局協議中）。Wayve Series D $1.5B（2026.2）の三社出資（Mercedes/Stellantis/Nissan）の一角。車載 IVI 内 LLM 搭載は [未特定]。Wayve は ADAS 重点で IVI Agentic AI への適用は限定的。Honda 共通OS研究の継続パートナー。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | 次世代 ProPILOT（Wayve基盤 FY2027）+ ロボタクシー Tokyo 2026末 [一次] |
| 量産時期 | Wayve 2027 / Tokyo Robotaxi 2026末 [一次] |
| 対象国 | グローバル + 日 [一次] |
| AI Agent搭載総台数 | [未特定] |
| FM Level | A（Wayve AI Driver = Embodied AI、車載 IVI LLM [未特定]）|
| 主要採用FM | Wayve AI Driver（Embodied AI）[一次] |
| 採用Orchestrator | Wayve（外部）+ NissanConnect [推論] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆 [一次]
- 旗艦モデルの市場定位：次世代 ProPILOT が Wayve 基盤、FY2027 量産
- 量産時期と地域戦略：日本先行（Tokyo Robotaxi 2026末）+ グローバル [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | コックピット制御（ProPILOT 経由）[推論] |
| 体験の深さ | Embodied AI（経験から学ぶ自律走行、事前プログラムなし）[一次] |
| 個別最適化度 | [未特定] |

UXシナリオ要約：
Wayve AI Driver で「経験から学ぶ」自律走行（事前プログラムなし）[一次]。IVI 内対話Agent は [未特定]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-T、Multi-Agent 空欄（Wayve ADAS のみ）[一次]
- 分類根拠：Wayve（外部 ADAS）+ NissanConnect（自前 IVI 既存）[推論]

### 3.2 Foundation Model レベル分析
- FM Level：A（Wayve API利用 + 車載 IVI LLM 別、[未特定]）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Wayve AI Driver（Embodied AI）[一次] |
| 採用Orchestrator | Wayve（外部）+ NissanConnect [推論] |
| 採用ミドルウェア（IVI OS）| NissanConnect [推論] |
| 採用チップ（SoC）| NVIDIA（Wayve基盤）+ Microsoft（Wayve）[一次] |
| R&D投資規模（AI関連年額）| Wayve に三者出資（Series D）[一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Wayve（ADAS）+ 車載 IVI LLM [未特定] |
| Orchestrator提供 | Wayve + 自社 |
| Chip提供 | NVIDIA |
| データ・地図提供 | [未特定] |
| ADAS提供 | Wayve（FY2027 量産、Tokyo Robotaxi 2026末）[一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | [未特定]（Wayve は ADAS のみ）|
| a-2 ナビ・ルート | 部分実装 |
| a-3 コックピット制御 | 2027（Wayve量産）|
| a-4 乗員ケア | 無 |
| a-5 コマース | 無 |

- 2027予測：P3-T 継続（Wayve 量産投入）
- 2030予測：P3-E（Wayve 全車展開 + Tokyo Robotaxi 商用化）

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- Wayve は西側 OEM 3社（Mercedes/Stellantis/Nissan）の共通 ADAS 基盤化。Honda が Wayve 採用に踏み切る選択肢の妥当性
- Tokyo Robotaxi（Wayve+Nissan+Uber）は日本での Robotaxi 商用化の試金石。Honda が日本市場で類似戦略を取る場合の先行事例

### 6.2 警鐘 or 注意点
- Nissan は IVI 内 Agent が [未特定] のまま ADAS に注力。Honda が ASIMO OS で IVI Agent を先行させる差別化が機能する余地

### 6.3 Honda の現在地との差分
Honda P2-T（ASIMO OS + Gemini + Helm.ai）と Nissan P3-T（NissanConnect + Wayve）の差は IVI Agent の重視度合い。Honda は IVI 側で先行、Nissan は ADAS 側に集中。

---

## 7. [未特定] 残課題

- Nissan Wayve 統合の課金モデル / Wayve 出資シェア（理由：$1.5B Series D 三社（Mercedes/Stellantis/Nissan）出資シェア未開示）
- 車載 IVI 内 LLM 搭載状況（理由：[未特定]）
- Tokyo Robotaxi の商用化時期（理由：当局協議中）
- 2026 大量負債償還への対応（破産懸念は分析筋から）

## 8. 2026 Q1-Q2 追加ファクト

- 過去四半世紀最深の財務危機継続：直近四半期 損失 倍増、FY2026 黒字復帰目標 [二次]
- **新型車開発期間を 50ヶ月→37ヶ月 に短縮**（消費者トレンド・競争激化への対応）[二次]
- 2026 大量負債償還を控える（一部アナリストは破産懸念を指摘）[二次]
- Wayve 採用：UK 自動運転ソフトウェア。Nissan ブランドで full integration、ProPILOT 次世代として位置づけ [二次]
- **Honda 統合協議は 2025.2 に決裂済**：governance dispute（Honda が Nissan を子会社化する案）に Nissan が反発。MOU は 2024.12.23 締結のみで未進展 [二次]

## 出典（2026 Q1追加）

- [ION Analytics — Nissan CFO outlines strategic reset](https://ionanalytics.com/insights/mergermarket/nissan-cfo-outlines-strategic-reset-partnership-priorities-amid-tariff-turmoil/) [二次]
- [CBT News — Nissan accelerates product launches](https://www.cbtnews.com/nissan-accelerates-product-launches-as-it-battles-the-worst-financial-crisis-in-decades/) [二次]
- [Motor Finance Online — Nissan walks away from Honda merger talks](https://www.motorfinanceonline.com/features/nissan-walks-away-from-honda-merger-talks-leaving-future-uncertain/) [二次]
