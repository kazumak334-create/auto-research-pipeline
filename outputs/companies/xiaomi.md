# Xiaomi — IVI Agentic AI 実装ファクトブック

**Tier：** T1
**分類：** P1-E（A' 親グループ流用＋自社・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026 SU7新型受注40K超、3月販売20K超、2026年550K台目標、2027年欧州展開・元Tesla中国GMをCAR販売責任者に登用
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Carnewschina（2026.4.3）

---

## 1. エグゼクティブサマリ

Xiaomi は MiMo を MIT License で GitHub 公開する自社 FM と HyperOS（Android 16 ベース）を組み合わせ、スマホ・家電・車を「最大10億デバイス」横断で統合する。EV を「最大の IoT ノード」と位置付け、2026 年 550K 台目標、SU7 累計500K超（2025.11、20ヶ月達成）。Tesla の P1-E と並ぶ完全垂直だが、エコシステム連結度では Tesla を上回る。Honda にとって最重要参照は「Person × Auto × Home」垂直統合の到達速度。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | SU7/YU7/SU7 Ultra（次世代SU7 902km CLTC, 2026）[一次] |
| 量産時期 | MiMo 2025.4〜 / Super XiaoAi HyperOS 2025.9〜 [一次] |
| 対象国 | 中国メイン、欧州 2027予定 [推論] |
| 旗艦年産 | SU7 累計500K超（2025.11時点、20ヶ月）[一次] |
| AI Agent搭載総台数 | 2026目標 550K [一次]、累計 2027 1M+ [推論] |
| FM Level | B〜C（自社FM MiMo + HyperOS Orch）|
| 主要採用FM | MiMo（自社、MIT License、V2.5-Pro public beta 2026.4.22）[一次] |
| 採用Orchestrator | HyperOS Orchestration 内製 [一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：高級 EV/SUV（YU7 Max 2026）+ 量販 SU7 [一次]
- 旗艦モデルの市場定位：SU7 累計500K超を 20ヶ月で達成。Tesla Model 3 を上回る加速度 [一次]
- 量産時期と地域戦略：中国先行、HyperOS 3（Android 16ベース）2026順次展開、欧州2027 [推論]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事（家×職場×車）+ コマース [一次] |
| 体験の深さ | 自律タスク実行（Miclaw 50+Tool、Super Tasks）[一次] |
| 個別最適化度 | 家・職場連結（HyperOS × Mi Home）[一次] |

UXシナリオ要約：
スマホで設定したスケジュールが車に連携、フードオーダーを車内で完結する [一次]。HyperOS 横断 80+ アプリを Super XiaoAi が一括処理。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P1-E × Multi-Agent ◎
- 分類根拠：Orchestrator・FM・OS すべて自前。チップのみ NVIDIA + Qualcomm 外部依存 [推論]

### 3.2 Foundation Model レベル分析
- FM Level：B〜C（MiMo は自社設計だが OSS との混合）
- 6要素配分：
  - アーキテクチャ：自前（MiMo）
  - ウェイト：Full学習（V2-Flash 2025.12 → V2-Pro / V2.5-Pro 2026.4.22）
  - 事前学習データ：自社収集 + 一部OSS [推論]
  - Fine-tuningデータ：自社（Mi Home 10億デバイス + SU7 フリート）[一次]
  - 学習インフラ：自社一部（Lei Jun 直轄 AI 戦略、規模 [未特定]）
  - 推論ランタイム：自社一部（HyperOS 内）+ NVIDIA Thor [推論]

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | MiMo（自社、MIT License、V2.5-Pro public beta 2026.4.22）[一次] |
| 採用Orchestrator | HyperOS Orchestration 内製 [一次] |
| 採用ミドルウェア（IVI OS） | HyperOS 3（Android 16ベース、2026年順次展開）[一次] |
| 採用チップ（SoC） | NVIDIA DRIVE Thor（2025末〜）+ Qualcomm 8295P [推論] |
| R&D投資規模（AI関連年額） | 全社 R&D [未特定]、Lei Jun 直轄AI戦略 [一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | 自社（MiMo、GitHub MIT公開）[一次] |
| Orchestrator提供 | 自社（HyperOS）[一次] |
| Chip提供 | NVIDIA（Thor）+ Qualcomm（8295P）[推論] |
| データ・地図提供 | Amap / Baidu Maps [推論] |
| ADAS提供 | 自社（XLA + MiMo-Embodied 統合）[一次] |
| 親グループ（P4のみ）| Xiaomi Group（HyperOS 共有）[一次] |

---

## 5. 将来：どこへ向かうか

### 5.1 内製意志（戦略宣言ファクト）
- 公式宣言：Lei Jun 直轄AI戦略（具体声明日付 [未特定]）。MiMo は GitHub MIT License 公開 [一次]
- 投資規模：全社 R&D [未特定]。"Person × Auto × Home" Great Convergence 戦略で HyperOS が10億デバイス統合
- 移行ロードマップ：MiMo V2-Flash（2025.12）→ V2-Pro / V2.5-Pro（2026.4.22 public beta）[一次]、HyperOS 3（2026順次展開）[一次]
- 動機：エコシステム差別化（スマホ × 家電 × 車）+ 自社FM コスト + コミュニティ（GitHub MIT 公開）

### 5.2 2027/2030 戦略パターン遷移予測
- 現在：P1-E（A' 親グループ流用 + 自社）
- 2027：P1-E（HyperOS 3 + MiMo V3）（確度：高）
- 2030：P1-E（"Person × Auto × Home" 完成、欧州展開拡大）（確度：高）
- 分岐条件：欧州規制壁 or 国内BYD/Li Auto 価格圧迫で利益率低下

### 5.3 in-Car 5観点 実装ステータス

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（Super XiaoAi HyperOS、Miclaw V2-Pro 50+Tool）[一次] |
| a-2 ナビ・ルート | 実装済（HyperOS 1.10.0 高速ナビ最適化、Super Tasks）[一次] |
| a-3 コックピット制御 | 実装済（XLA + MiMo-Embodied で Lvl2+ 自動化）[一次] |
| a-4 乗員ケア | 2026予定（MiMo-Embodied 拡張）[推論] |
| a-5 コマース | 実装済（フードオーダー、HyperOS 横断 80+アプリ）[一次] |

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- スマホ・家電エコシステム保有がない Honda にとって、Xiaomi 型は再現不能。逆に「Honda のエコシステム不足」を可視化する負の参照
- MIT License で FM をコミュニティ公開する戦略は、自前FM 開発コストを開発者貢献で相殺する手法。Honda が ASIMO OS の一部レイヤーを公開する余地の検討材料

### 6.2 警鐘 or 注意点
- Xiaomi の参入から20ヶ月で 500K 台到達。「自動車製造の参入障壁」が低下した実例。Honda が自動車業界既存ポジションを優位と見なす前提が崩れる
- 中国国内市場依存度が高く、欧州規制で減速する可能性。グローバル展開リスクは中

### 6.3 Honda の現在地との差分
Honda の P2-T（ASIMO OS + Gemini）から Xiaomi P1-E への到達距離は大（自社FM・スマホエコシステム未保有）。エコシステム横断は Honda 単独では困難で、Sony や au 等との連携が前提。

---

## 7. [未特定] 残課題

- Xiaomi 全社 R&D 投資規模・AI 専門組織人員（理由：Lei Jun 直轄は確認、規模は IR 非開示）
- HyperOS 欧州展開時の規制対応（理由：[未特定]）
- MiMo V2.5-Pro の量産車での Tool Use カバー範囲（理由：public beta 段階）

## 8. 2026 Q1-Q2 追加ファクト

- 2026年販売目標 550K 台（前年比 +34%）[一次]
- 2026年4-6種 新車発売予定（純電 + EREV 2系統）、価格帯 20万〜55万元、SUV/sedan + 5/7人乗りカバー [一次]
- 新型SU7 受注 40K超（2026.4.2 時点）、3月納車超 20K（うち新SU7 7K、2026.3.23 出荷開始）[一次]
- YU7 待ち時間 33-56週 → 7-14週に短縮（受注減速の兆候）[二次]
- 2026.3 Kong Yanshuang（元 Tesla 中国 GM）を自動車販売責任者に登用 [二次]
- 海外展開：2027 欧州先行 [一次]

## 出典（2026 Q1追加）

- [Carnewschina — Xiaomi SU7 40,000 firm orders](https://carnewschina.com/2026/04/03/xiaomi-autos-new-su7-receives-40000-firm-orders-amidst-ambitious-2026-product-expansion/) [二次]
- [Autoblog — Xiaomi 550,000 vehicle goal](https://www.autoblog.com/news/xiaomi-eyes-550000-vehicle-sales-goal-as-auto-push-accelerates) [二次]
