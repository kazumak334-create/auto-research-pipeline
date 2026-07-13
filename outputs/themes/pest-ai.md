# PEST分析: AI産業（生成AI・基盤モデル・AIインフラ）
**フレーム:** PEST × AGI移行リスク × 企業競争構造  
**最終更新:** 初版（2026-05-11）  
**更新者:** auto-agent

---

## 概要・主要論点

生成AIは「研究フェーズ」から「大規模産業実装フェーズ」に移行中（2024-2026年）。
基盤モデル競争（OpenAI / Google / Anthropic / Meta / xAI / 中国勢）× AIインフラ投資（$600B+宣言）× 規制枠組み形成が同時進行。
収益化格差（BtoBエンタープライズ進展 vs BtoCマネタイズ難）が企業間淘汰の主軸。

**2026年5月時点のキーナンバー:**

| 指標 | 数値 |
|------|------|
| 生成AI市場規模 | ~$150B（2025年推計） |
| Microsoft / Google AI関連CAPEX | 各社$50B+/年 |
| OpenAI 年間収益 | ~$3.4B（2024年）→$10B+（2025年推計） |
| EU AI Act 高リスクシステム規制 | 2025年8月施行 |
| 中国AI企業数（基盤モデル） | 約130社（2025年末時点） |

---

## P: 政治・規制 (Political)

### 主要監視テーマ
- EU AI Act：リスク分類（禁止／高リスク／限定リスク）の実装・産業影響
- 米国大統領令（AI安全・セキュリティ）：バイデン→トランプ政権での規制方向転換
- 中国AI規制：生成AIサービス規制（2023年）/ ディープシンセシス規制 / アルゴリズム規制
- G7/G20 AI ガバナンスフレームワーク（広島AIプロセス後継）
- AI著作権問題：米国・EU・日本での立法動向
- AIの軍事・安全保障利用規制（自律型兵器システム）

### 検索クエリテンプレート（{YYYY-MM}を当日年月に置換）
```
EU AI Act implementation enforcement {YYYY-MM} site:reuters.com OR site:ft.com
US AI policy regulation executive order {YYYY-MM}
China AI regulation generative AI governance {YYYY-MM}
G7 AI governance Hiroshima process {YYYY-MM}
AI copyright legislation US EU Japan {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: Anthropic Claude Opus 4.7リリース。年間収益ランレート$30B超。Trump政権、Google/MS/xAI AIモデルの政府評価合意。

---

## E: 経済 (Economic) ※マンキュー変数ベース

### マクロ変数→AI産業への波及
| マンキュー変数 | AI産業への影響 |
|-------------|--------------|
| 高金利環境 | AIスタートアップ資金調達コスト上昇・バリュエーション圧縮 |
| AI投資乗数 | AI設備投資→短期GDPには貢献、長期生産性向上は未確認 |
| 労働市場 | AIによるホワイトカラー労働代替が失業率統計に反映されるタイムラグ |
| ドル高 | 米国AI企業の海外収益換算増加、欧州企業の競争力相対低下 |

### 産業固有経済指標
**監視ポイント:**
- 大手テック CAPEX（Microsoft / Google / Amazon / Meta）：AI GPU投資実額
- OpenAI / Anthropic 年間収益・月次ARR成長率
- AI推論コスト：$/1M tokens の下落速度（規模の経済 vs モデル効率化）
- エンタープライズAI導入率：Fortune 500でのCopilot / Gemini Enterprise導入
- AI関連VC投資：ステージ別・地域別資金フロー

**検索クエリ:**
```
Microsoft Google Amazon Meta AI CAPEX investment {YYYY-MM} quarterly earnings
OpenAI Anthropic revenue ARR growth {YYYY-MM}
AI inference cost per token decline {YYYY-MM}
enterprise AI adoption Copilot Gemini {YYYY-MM}
AI startup funding venture capital {YYYY-MM} site:pitchbook.com OR site:crunchbase.com
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: EU AI Act 2026年8月完全施行迫る。一部高リスク要件は2027-2028年に延期交渉中。米国は連邦統一AI法案非拘束フレームワークのみ。

---

## S: 社会・労働市場 (Social)

### 主要監視テーマ
- ホワイトカラー労働代替：コーディング / 法務 / 財務分析 / カスタマーサポート
- AI信頼性：ハルシネーション・バイアス問題への社会的対応
- デジタルデバイド：AI利用格差（先進国 vs 途上国 / 富裕層 vs 中間層）
- 教育変革：大学・企業研修でのAIスキル要求急増
- 創作産業への影響：アーティスト・ライター・クリエイターの収益モデル崩壊
- 人口動態 × AI：少子高齢化社会でのAI補完需要（特に日本）

### 検索クエリテンプレート
```
AI job displacement white collar employment survey {YYYY-MM}
AI trust hallucination bias society {YYYY-MM}
AI skills education workforce training {YYYY-MM}
generative AI creative industry impact writers artists {YYYY-MM}
AI aging society Japan demographic {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: Google Cloud Q1 +63%で$20B、AI生成製品収益+800%。Azure +40%で$34.7B。Big Tech AI Capex合計~$700B。

---

## T: 技術 (Technological)

### 主要監視テーマ
**基盤モデル競争:**
- OpenAI：GPT-4o以降・o3推論モデル・AGI主張の検証
- Google：Gemini Ultra 2.0 / Project Astra（マルチモーダルエージェント）
- Anthropic：Claude 4系の能力向上・Constitutional AI実装
- Meta：LLaMA 4系オープンソース展開・コミュニティエコシステム
- 中国勢：DeepSeek R2 / Qwen3 / Baidu ERNIE 4.0

**アーキテクチャ・効率化:**
- 推論効率：MoE（Mixture of Experts）→ 少ないパラメータで高性能
- テスト時計算（Test-Time Compute）：o3型の強化学習推論
- マルチモーダル：テキスト + 画像 + 音声 + 動画 + コードの統合
- エージェント：自律的タスク実行（Computer Use / Tool Use）

**インフラ:**
- NVIDIABlackwell GB200 NVL72供給状況
- カスタムASIC：Google TPU v5 / Amazon Trainium / Microsoft Maia
- エッジAI：スマートフォン・車載での推論（Apple A18 / Qualcomm Oryon）

### 検索クエリテンプレート
```
GPT OpenAI model benchmark update {YYYY-MM}
Google Gemini Anthropic Claude model release {YYYY-MM}
DeepSeek Qwen Chinese AI model performance {YYYY-MM}
AI agent autonomous computer use {YYYY-MM}
NVIDIA Blackwell GPU supply AI infrastructure {YYYY-MM}
edge AI on-device inference smartphone {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: DeepSeek V4-Pro（1.6Tパラメータ）プレビューリリース。Huawei Ascend 950活用。MIT License、競合比4倍安価。

---

## 企業別競争ポジション概観

| 企業 | 強み | 主要リスク |
|------|------|-----------|
| OpenAI | 先行者優位・ブランド・API生態系 | 規制リスク・資金依存・競合追い上げ |
| Google DeepMind | 検索統合・TPU垂直統合・データ | AI検索侵食・独禁リスク |
| Anthropic | 安全性ブランド・エンタープライズ | 規模の劣後 |
| Meta | オープンソース戦略・広告データ | プロプライエタリ技術流出 |
| Microsoft | エンタープライズ統合（Copilot365） | OpenAI依存リスク |
| NVIDIA | AI GPU独占的地位（H100/B200） | 競合ASIC台頭・輸出規制 |
| DeepSeek/中国勢 | コスト効率・中国市場 | 輸出規制・データ懸念で国際展開制限 |

---

## 更新ログ

| 日付 | 更新内容 | 更新者 |
|------|---------|--------|
| 2026-05-11 | 初版作成。基盤モデル競争・AI規制・労働代替の3軸でPEST設計 | auto-agent |
| 2026-05-13 | 最新動向追記 | auto-agent |

## 最新動向

### 2026-05-13
- **[Political]** Trump-Xi 首脳会談（5/14-15北京）でAI安全保障が主要議題。「AIにおけるデコンフリクション・チャンネル」の設置を米国が検討
- **[Political]** EU AI Act が金融サービス向けに適用開始。高リスクAI（信用スコアリング等）は人間監督・データガバナンスが義務化
- **[Technology]** Perceptron Mk1（動画解析AI）が Anthropic/OpenAI/Google 比 80-90% 安価な価格で高性能を実現。物理AI推論分野の新競合
- **[Technology]** Microsoft Azure 40% YoY成長 vs Google Cloud 28%。Copilot有償化で企業AI収益化でMSFTが先行
- **[Social]** 米国人の50%がAIに懸念を示す（Pew調査）、G7平均33%。中国は「AIに置き換えられる恐怖が採用を加速」と逆方向
- **[Technology]** DeepSeek 最新モデルが米国チップへの依存をさらに低減。中国AIモデルの性能差が「実質消滅」とStanford研究が報告

### 2026-07-14 更新
- **中国AI vs 米国**: OpenRouterで米国企業の中国AIモデル利用率が週次30%超（ピーク46%）。DeepSeek/Z.ai GLM 5.2が性能・コスト比でAnthropicの60〜90%安。Lindy（AI startup）がAnthropic→DeepSeekに100%移行し数百万ドルのコスト削減。[CNBC 2026-07-07]
- **EU AI Act**: コンプライアンスと執行が焦点。グローバル規制の整合性リスク——企業が複数法域で異なる規律に対応必要。[Foley & Lardner 2026-07-08]
- **Meta Compute**: Metaがクラウドビジネス参入——AI計算資源をAWS/Azure/GCPに対抗して販売。CEO Zuckerberg、2026年度capex $115〜135B。Llama OSS＋カスタムハードをセットで提供。[Bloomberg/Yahoo Finance 2026-07-01]
- **DeepSeek V4**: DeepSeek V4-Pro/Flashをオープンソースでリリース（2026-04-24）。開発費<$6M。GLM 5.2はAnthropicのOpus 4.8に性能1%差で約1/5のコスト。
