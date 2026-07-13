# Li Auto — IVI Agentic AI 実装ファクトブック

**Tier：** T1
**分類：** P1-E（垂直完全・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ 2026年 +20% 成長目標、Q1納車減速見通し（購入税優遇縮小）、OTA 8.3 で VLA Driver+ Cockpit 大幅更新、L9次世代 Q2 2026 launch 予定
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Li Auto 公式（2026.3.12）

---

## 1. エグゼクティブサマリ

Li Auto は MindGPT（自社 FM、MoE+Sparse Attention）+ Lixiang Tongxue Agent（300+ Tool Use、120M件/日インタラクション）を量産投入する完全垂直 P1-E。MindVLA を「ロボット Large Model」と位置づけ、車を「ロボット端末」と定義した最初の量産OEM。R&D RMB 113億（2025通期）、2026通期目標 480K 台超。i8（BEV SUV、2025.8 量産）で空調・ワイパー含む全車載機能を Tool 化。Honda にとって「中国先行2年」の象徴であり、AGI 企業転身という野心の到達速度を示す事例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | i8（BEV SUV, 2025.7量産）/L9次世代（2026 Q2予定）[一次] |
| 量産時期 | i8 2025.8 / VLA 全AD Max 同時 [一次] |
| 対象国 | 中国（Lixiang Tongxue 海外展開未確定）[未特定] |
| 旗艦年産 | i8 月次 [未特定] / Li Auto 全体 2026目標 480K [一次] |
| AI Agent搭載総台数 | 2026 480K 全車AD Max 化 [推論] |
| FM Level | C（Full Stack型、自社 MindGPT MoE+Sparse Attention）|
| 主要採用FM | MindGPT（自社, MoE+Sparse Attention）+ DeepSeek 補完 [一次] |
| 採用Orchestrator | Lixiang Tongxue Agent 内製（300+ Tool Use）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：高級ファミリー SUV/MPV/EREV [一次]
- 旗艦モデルの市場定位：i8 が BEV 拡大の象徴、L9 系が EREV 主力。Q1 2026 累計 95,142台（≒目標 19.8%）[一次]
- 量産時期と地域戦略：中国国内集中、海外展開は未確定 [未特定]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事 + ロボット制御（i8 全機能 Tool 化）[一次] |
| 体験の深さ | 自律タスク実行（98.7%精度、Tongxue Agent 300+ Tool）[一次] |
| 個別最適化度 | 履歴学習＋家連結（Lixiang Tongxue 120M件/日）[一次] |

UXシナリオ要約：
"車内が暑い" という曖昧な指示で Tongxue Agent が空調 + 窓開け + サンルーフを一括判断する [一次]。複合的な乗員意図を Agent が解釈・分解して実行。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P1-E × Multi-Agent ◎
- 分類根拠：MindGPT（自社FM）+ Tongxue Agent（自社Orch）+ Li OS（自前）。チップは NVIDIA Orin-X / Thor-U 外部依存だが他は完全自前 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：C（Full Stack型）
- 6要素配分：
  - アーキテクチャ：自前（MindGPT MoE+Sparse Attention）
  - ウェイト：Full学習
  - 事前学習データ：自社収集（Lixiang Tongxue 120M件/日）
  - Fine-tuningデータ：自社（フリート全車AD Max 走行データ）
  - 学習インフラ：自社（R&D RMB 113億）
  - 推論ランタイム：自社（Tongxue Agent + Li OS）+ NVIDIA Thor-U 700 TOPS

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | MindGPT（自社, MoE+Sparse Attention）+ DeepSeek 補完 [一次] |
| 採用Orchestrator | Lixiang Tongxue Agent 内製（300+ Tool Use）[一次] |
| 採用ミドルウェア（IVI OS）| Li OS（自前、AAOS 派生 [推論]）|
| 採用チップ（SoC）| NVIDIA Orin-X / Thor-U（700 TOPS）[一次] |
| R&D投資規模（AI関連年額）| RMB 113億（2025通期）[一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | 自社 MindGPT + DeepSeek 補完 [一次] |
| Orchestrator提供 | 自社（Tongxue Agent）[一次] |
| Chip提供 | NVIDIA（Orin-X / Thor-U）[一次] |
| データ・地図提供 | Amap（Alibaba 系、Mobility AI Agent 世界初OEM採用）[一次] |
| ADAS提供 | 自社（VLA / MindVLA）[一次] |
| 親グループ（P4のみ）| Li Auto Inc.（独立、米Nasdaq + 香港）[一次] |

---

## 5. 将来：どこへ向かうか

### 5.1 内製意志（戦略宣言ファクト）
- 公式宣言：CEO Li Xiang 自身が AI戦略フルコミット（2025.2 経営体制再編）[一次]、「AGI カンパニーへの転換」+ ヒューマノイドロボット開発 [一次]
- 投資規模：R&D RMB 113億（2025通期）[一次]、Lixiang Tongxue 120M件/日インタラクション [一次]
- 移行ロードマップ：MindVLA = ロボット Large Model（NVIDIA GTC 2026.3）[一次]、3D ViT Encoder 統合、人間レベル空間認識 [一次]、Smart Glasses Livis（2025.12 launch、AI capabilities 拡張）[一次]
- 動機：差別化（ロボット端末化）+ データ主権 + 完全垂直で価格競争力 [推論]

### 5.2 2027/2030 戦略パターン遷移予測
- 現在：P1-E（垂直完全 + Multi-Agent）
- 2027：P1-E（MindVLA + Robot Large Model + Livis）（確度：高）
- 2030：P1-E（AGI企業確立、ロボティクス領域拡大）（確度：高）
- 分岐条件：海外展開（英米）+ ロボット事業の独立性 = リスク要因

### 5.3 in-Car 5観点 実装ステータス

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（Tongxue Agent、120M件/日、月次使用率 91% 2025.10）[一次] |
| a-2 ナビ・ルート | 実装済（Amap Mobility AI Agent、世界初OEM採用）[一次] |
| a-3 コックピット制御 | 実装済（i8 全機能 Tool 化：空調・ワイパー含む）[一次] |
| a-4 乗員ケア | 2026予定（MindVLA 拡張）[推論] |
| a-5 コマース | 実装済（Tongxue + 充電 4,054ステーション統合）[一次] |

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 「全車載機能の Tool 化」が量産可能であることを証明。Honda の ASIMO OS が目指すべき到達点として最も具体的
- Tool Use 300+ のスケールは Honda 0 Series 単独では時間的に追いつけず、初期はサブセット（50-100 Tool）から開始する現実的ターゲット設定が必要
- Amap Mobility AI Agent 採用は「地図プロバイダーの Agent 化」が始まった象徴。Honda の地図戦略（Google Maps 依存）を再検討する材料

### 6.2 警鐘 or 注意点
- 中国先行2年の象徴。Honda が同等機能を2027以降に展開しても「2年遅れ」は数値で見える化される
- 「車をロボット端末と再定義」する戦略宣言は、自動車産業の枠を超えた競合構造の変化を示す。Honda がロボティクス領域でも勝負する選択肢を保有する必要

### 6.3 Honda の現在地との差分
Honda の P2-T（ASIMO OS + Gemini）から Li Auto P1-E への到達距離は超大（自社 FM・自社 ADAS・自社チップロードマップ未保有）。再現は困難だが「全機能 Tool 化」という UX 目標は転用可能。

---

## 7. [未特定] 残課題

- Lixiang Tongxue 量産車内搭載のDeepSeek 統合範囲（理由：スタンドアローンApp は確認、量産車コックピット標準搭載か別系統か未確認）
- 海外展開（英米）の具体的計画・時期（理由：[未特定]）
- MindGPT の MoE 専門家数・Sparse Attention 技術仕様（理由：論文化されていない）
- ロボティクス事業の独立法人化の有無（理由：[未特定]）

## 8. 2026 Q1-Q2 追加ファクト

- 2025年通期納車 -18.8% YoY（実績下振れ）→ 2026年 +20% 成長目標に修正 [一次]
- 2026年2月納車 26,421台（累計 1,594,304台）[一次]
- 中国の購入税優遇 phase out で Q1 2026 「substantial dip」見通し [二次]
- OTA 8.3（春節前リリース）：VLA Driver / Smart Cockpit / Smart EV 三領域大幅更新 [一次]
- VLA model 性能改善「ChatGPT 3.5 → 4.0 相当」自社主張、販売へのインパクト要証明 [一次]
- 全新 Li L9 を 2026 Q2 launch 予定 [一次]
- Starry Ring OS / VLA / MindGPT の3本柱戦略を維持 [一次]

## 出典（2026 Q1追加）

- [CnEVPost — Li Auto sets 20% growth goal for 2026](https://cnevpost.com/2026/03/12/li-auto-sets-20-growth-goal-for-2026/) [二次]
- [StockTitan — Li Auto February 2026 deliveries](https://www.stocktitan.net/news/LI/li-auto-inc-february-2026-delivery-59vimkg9csue.html) [一次]


## 直近アップデート
- 2026-05-11: 2026年目標55万台配達、REEV重視路線継続。4月34,085台 (+0.4%)。 ([出典](https://cnevpost.com/2026/01/21/li-auto-aims-550000-sales-2026-increased-focus-erevs/))

### 2026-05-13
- 事実：Li L9 Livis（旗艦SUV）5月15日正式発売。自社開発5nmチップM100×2搭載（2,560 TOPS）、LiDAR×4、559,800元
- 出典：https://cnevpost.com/2026/04/24/li-auto-to-officially-launch-l9-livis-may-15/
- 発表日：2026-04-24
- 確度：中（industry_media）
- 2026-07-14: 2026年6月配送30,895台（-14.84% YoY）。2ヶ月連続前年比減。 ([出典](https://autonews.gasgoo.com/articles/news/li-xiang-ai-and-embodied-intelligence-are-not-a-diversion-for-li-auto-2065696772075405313))
