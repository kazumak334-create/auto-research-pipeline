# Toyota — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** 段階2 移行中（Orch [未特定]・量産前）
**最終更新：** 2026-05-01
**更新履歴：**
- 2026-04-28：初版作成（Arene OS 第1号 RAV4、Azure OpenAI O-Beya）
- 2026-05-01：KB追加（トヨタ対中国EV/中西孝樹）。Arene OS の層位置を修正（Layer 3 / IVI Platform）。Orch Layer 5 は [未特定] に変更。OTA サイクル・AIDV ギャップ・3本柱・RCE制度を追加。分類を P2-T から「段階2 移行中（Orch [未特定]）」に更新。

**ソース：** 04a_market-raw_v2.md + Toyota Newsroom + Autonews + kb-トヨタ対中国EV.md（中西孝樹、2025）

---

## 0. 重要注記：Arene OS の層位置

> **Arene OS は IVI プラットフォーム層（Layer 3）であり、Orchestrator 層（Layer 5）ではない。**

| 確認内容 | 根拠 |
|--------|------|
| Arene OS = SDV向けOS（SDK / Tools / Data の3機能を持つ、オープン設計）| KB p.206「Areneはオープンな開発環境であり、外部の開発者・企業・サプライヤーが活用できるプラットフォームとして設計されている」[二次] |
| IVI スタック定義 Layer 3（IVI Platform）の例示に「Arene」が含まれる | 00_definitions.md 定義1「MB.OS／HyperOS／STLA Brain／**Arene**／Cerence xUI」[一次] |
| Orchestrator 層（Layer 5）の実装状況 | [未特定]。C1/C2/C3 を満たす Orch の存在は公表なし |

→ **Toyota の Orch 自前判定（C1/C2/C3）は現時点で [未特定]。「段階2 移行中」で維持するが「Orch 自前確定」とは言えない。**

---

## 1. エグゼクティブサマリ

Toyota は Arene OS（Woven by Toyota 共同開発）を自前 SDV プラットフォームとし、2026 Q1 RAV4 で Layer 3（IVI Platform）として第1号量産投入。Orchestrator 層（Layer 5）の自前実装は [未特定]。車載 FM は Azure OpenAI GPT-4o（O-Beya）が内部開発支援用として先行するが、車載量産 FM は [未特定]。NTT との 500億円 Mobility AI Platform（2025開発・2028実装）が次の主軸。

**AIDV（AI定義型自動車）への進化が必要**だが、OTA 更新サイクルは日系標準の3〜6ヶ月で中国勢（2週間）との差が開いている。HEV + Arene OS + 全固体電池（2027〜2030年代）の「3本柱」でSDV時代の競争力回復を目指す。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | RAV4 2026（Arene 第1号 / TSS 4.0 + Multimedia 新世代）[一次] |
| Arene 量産投入 | 2026 Q1（北米 2月〜）[一次] |
| 対象国 | グローバル（HEV 含む RAV4）[一次] |
| AI Agent 搭載台数 | [未特定] |
| FM Level（車載）| [未特定]（O-Beya = Azure OpenAI GPT-4o は内部用）|
| 主要採用 FM | Microsoft Azure OpenAI（GPT-4o / O-Beya、内部 AI 開発支援用）[一次]。車載 [未特定] |
| Arene OS の層位置 | **Layer 3（IVI Platform）**。Orchestrator（Layer 5）は [未特定] |
| OTA 更新サイクル | 3〜6ヶ月（日系標準）。中国勢（2週間）との格差あり [KB・推計] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 全体戦略方針

**ZEVON 視点**（知識ベース）：
中西孝樹の ZEVON 概念に照らすと、Toyota の競争力は「電動化（EV）」には一定の手当てがあるが「知能化（AI/SDV/ADAS）」の速度が中国勢に後手に回っている状態。

**3本柱（Toyota の SDV 競争力回復戦略）：**
1. **GA-K プラットフォーム**：次世代 EV/HEV 共通プラットフォーム
2. **Arene OS**：SDV 向け OS（Layer 3 / IVI Platform）。オープン設計で外部開発者が利用可能
3. **全固体電池**：Toyota は 2027〜2030年代量産目標（BYD は 2027〜28年目標）[KB・一次]

### 2.2 地域別戦略

**中国戦略「油電同強（ICE と EV を同等の競争力に）」：**
- 中国専用開発体制を強化。RCE（地域チーフエンジニア）制度を導入し開発サイクル 4年以上→約2年に短縮目標 [KB・一次]
- 2024年時点で中国 EV 市場での苦戦が続く。現地化スピードが競争力の核心

**HEV 戦略（グローバル）：**
- マルチパスウェイ戦略：HEV / PHEV / BEV / FCEV を地域ニーズに応じて使い分け
- 充電インフラ未整備の新興国・地方では HEV が有効 [KB]
- **Honda との競合領域**：HEV 強化路線は Honda と直接重複

### 2.3 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | ナビ強化 + Multimedia（RAV4 2026）[一次] |
| AIDV 対応 | 未到達。AI がユーザー好みを学習・進化する「AIDV（AI 定義型自動車）」は将来目標 [KB] |
| OTA 更新频度 | 3〜6ヶ月（日系標準）。AIDV 実現には2週間サイクル相当の速度化が必要 [KB・推計] |

---

## 3. アーキテクチャ：どう作るか

### 3.1 IVI スタック6層における Toyota の位置

| Layer | 名称 | Toyota の実装 | 確度 |
|-------|------|------------|------|
| 6 | Application | 対話 UI（RAV4 2026 搭載）| [一次] |
| 5 | **Orchestrator** | **[未特定]**。Arene OS が Orch 機能を含むか不明 | [未特定] |
| 4 | Foundation Model | 車載 [未特定]。O-Beya（Azure OpenAI GPT-4o）は内部開発支援用 | [一次] |
| 3 | **IVI Platform** | **Arene OS**（Woven by Toyota 共同開発、SDK/Tools/Data）| [一次] |
| 2 | OS 層 | Linux 系？詳細 [未特定] |  |
| 1 | チップ層 | [未特定] / NTT Mobility AI Platform 開発中 | [一次] |

**Arene OS の詳細（KB 追加）：**
- SDK（ソフトウェア開発キット）/ Tools（開発ツール群）/ Data（車両データ活用）の3機能
- オープンな開発環境。外部の開発者・企業・サプライヤーが活用可能 [KB p.206]
- Woven by Toyota と共同開発。2025年以降段階的に車両搭載 [KB]

### 3.2 Orchestrator 自前判定（C1/C2/C3）

| 条件 | 判定 | 根拠 |
|-----|------|------|
| C1 仕様策定責任（コア3要素が社内）| [未特定] | Arene OS が Orch コア3要素を含むか未公表 |
| C2 実装制御（主要部分が社内）| [未特定] | 同上 |
| C3 進化制御（将来変更が社内意思決定）| [未特定] | 同上 |
| **総合判定** | **[未特定]** | Arene = Layer 3 確認、Layer 5 Orch は別実装か否か不明 |

**要調査：** Toyota の公式技術文書・CES / TMS 2025 発表資料で Orchestrator 機能の存在を確認すること。

### 3.3 FM Level

| Level | 判定 | 根拠 |
|-------|------|------|
| 車載 FM | [未特定] | O-Beya（内部用）と車載 FM は別。車載 FM の選定未公表 |
| O-Beya（内部用）| Level A（Azure OpenAI API 利用）| Microsoft 提携、エンジニア 70万人向け AI 開発支援 [一次] |

**E/Eアーキテクチャの世代（KB 追加）：**
- SDV 実現の前提技術は分散型→ドメイン型→ゾーン・セントリック型への移行
- Toyota は Arene 展開で SDV Lv.2〜3 移行中（詳細 [未特定]）

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 | 内容 |
|-------------|------|-----|
| FM提供（内部用）| Microsoft Azure OpenAI | GPT-4o / O-Beya 内部開発支援 [一次] |
| FM提供（車載）| [未特定] | — |
| SDV OS / Layer 3 | Woven by Toyota（自社グループ）| Arene OS 共同開発 [一次] |
| Orchestrator / Layer 5 | [未特定] | — |
| チップ | [未特定] / NTT 共同開発 | — |
| AI Platform | NTT | 500億円 Mobility AI Platform（2025開発・2028実装）[一次] |
| ADAS | Toyota Safety Sense 4.0（自前）+ Momenta（中国 Bozhi 3X）[一次] | — |

---

## 5. 将来：どこへ向かうか

### 5.1 ロードマップ

| 時期 | 内容 |
|-----|-----|
| 2026 Q1 | Arene OS（Layer 3）第1号搭載 RAV4 量産投入 [一次] |
| 2026 H2〜2027 | Arene OS 全車展開フェーズ |
| 2027〜28年 | 全固体電池量産目標（Toyota）。同時期 BYD も目標 [KB] |
| 2028 | NTT Mobility AI Platform 実装予定 [一次] |
| 2030年代 | 全固体電池本格普及、AIDV 移行完成？[KB・推論] |

### 5.2 AIDV 化への課題

**AIDV（AI 定義型自動車）** = AI がユーザーの行動・好みを学習し、車がユーザーに合わせて進化する「動く知能体」[KB p.091]

Toyota が AIDV に到達するために必要な要素：
1. Orchestrator（Layer 5）の自前実装（現在 [未特定]）
2. OTA 更新サイクルの大幅短縮（現在 3〜6ヶ月 → 目標 2週間以下）
3. ユーザー行動データの学習ループ構築
4. 車載 FM（Layer 4）の確定と継続進化体制

### 5.3 リカーリング収益モデル

SDV 時代の Toyota の収益転換方向 [KB p.202]：
- テレマティクス / AI アシスタント / OTA アップデート / コネクテッドサービス
- ウーブン・シティ（静岡）でのスマートシティ実証
- NTT Mobility AI Platform が 2028 以降のリカーリング収益基盤

---

## 6. Honda 示唆（So What）

### 6.1 HEV + AI 路線の直接競合

Toyota の HEV 強化 + Arene OS（Layer 3）+ 全固体電池の3本柱は Honda の HEV + AI 路線と市場が重複。

- 同一セグメント（HEV 中価格帯）で同質化すると、**Toyota の販売規模（年間約1000万台）> Honda（約400万台）** で Honda が不利
- Toyota が Arene + 全固体電池を組み合わせた「HEV + SDV」を実現した場合、Honda の差別化軸が必要

### 6.2 OTA サイクルが Honda の差別化機会

Toyota の OTA 更新サイクルは日系標準（3〜6ヶ月）のまま。中国勢（2週間）との差が競争上の弱点。

**Honda の機会：** OTA 更新サイクルを Toyota より速くできれば（例：1ヶ月サイクル）、HEV + AI 市場での一時的な差別化軸になりうる。[推論]

### 6.3 Honda 固有の差別化軸候補（仮）

| 軸 | 根拠 | Toyota との差分 |
|----|-----|--------------|
| 二輪 × 四輪エコシステム | Honda のみが持つモビリティ資産 | Toyota には二輪がない |
| 乗員ケア / ヘルスモニタリング | Honda Life Creation 領域 | Toyota の AIDV 設計では未確認 |
| 中小型モビリティへの AI 展開 | インド市場（Honda 強み）| Toyota はインドで普通車・HEV 主体 |

**これらはすべて仮説レベル。次フェーズで数値化・検証が必要。[仮]**

### 6.4 Arene OS からの学び

Arene のオープン設計（外部開発者が活用可能）は ASIMO OS の設計思想との比較材料になる。Honda の ASIMO OS がクローズド設計なら、エコシステム拡張性でトヨタに劣後するリスク。[推論]

---

## 7. [未特定] 残課題

| 項目 | 優先度 | 調査方法 |
|-----|------|----|
| Toyota Orchestrator 層（Layer 5）の自前実装有無 | **高**（V1 検証項目）| Toyota CES2025 / TMS2025 技術発表確認 + 公式技術文書 |
| 車載 FM の選定（Layer 4）| 高 | Toyota Newsroom + 提携発表確認 |
| Arene OS の Linux/Android 系の識別 | 中 | Woven by Toyota 公開資料 |
| OTA 更新サイクルの正確な数値 | 中 | Toyota Developer Blog / RAV4 2026 実績 |
| 全固体電池量産の進捗（2027目標の達成可能性）| 中 | Toyota IR（2026 Q1）+ 技術発表 |
| NTT Mobility AI Platform の Orch/FM との連携設計 | 低 | NTT × Toyota 共同発表資料 |

---

## 8. 参照 KB メモ

本ファイルへの追加情報ソース：`~/.claude/knowledge/kb-トヨタ対中国EV.md`（中西孝樹、2025）

| 概念 | KB 参照箇所 | 本ファイルへの反映 |
|-----|-----------|--------------|
| Arene OS の設計・機能 | p.206（第8章）| セクション0・3 |
| AIDV（AI 定義型自動車）| p.091（第4章）| セクション5.2 |
| OTA 更新サイクル（日系 3-6ヶ月 vs 中国 2週間）| p.181（第7章）| セクション1・6.2 |
| 3本柱（GA-K / Arene / 全固体電池）| 適用ルール 17 | セクション2.1 |
| 油電同強・RCE 制度（中国戦略）| p.179（第7章）| セクション2.2 |
| リカーリング収益モデル | p.202（第8章）| セクション5.3 |
| ZEVON（電動化 × 知能化）| p.003（序章）| セクション2.1 |


## 直近アップデート
- 2026-05-11: RAV4 2026 新ソフトウェア：将来EV向けの新UIプラットフォームの示唆。 ([出典](https://insideevs.com/news/775729/2026-toyota-rav4-phev-arene-software-ev/))

### 2026-05-13
- 事実：Toyota/Lexus が EV ロードトリップを改善（充電ネットワーク連携）。米国販売は4ヶ月連続前年比減
- 出典：https://electrek.co/2026/05/12/toyota-lexus-just-made-ev-road-trips-way-easier/
- 発表日：2026-05-12
- 確度：中（industry_media）
- 2026-07-14: 日系OEMのHEV利益軸とAI・SDV転換加速（HEV利益率優位を維持しながらEV移行）。[Digitimes 2026-07] ([出典](https://www.digitimes.com/news/a20260616PD233/automakers-toyota-honda-hev-nissan.html))
