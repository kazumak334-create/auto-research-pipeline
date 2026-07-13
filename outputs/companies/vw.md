# Volkswagen Group — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3→C hybrid（XPeng依存度上昇・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ CEA 量産開始（VW 2026.1.29発表、ID.UNYX 08）。2026年 春から CEA で5新型展開。XPeng VLA 2.0 を VW が初顧客（2026.3.2 launch、Robotaxi L4 へも展開）。CARIAD はパートナーソフト統合役へ縮退（Rivian + XPeng）
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Carnewschina（2026.1.29）+ Technode（2026.2.26）

---

## 1. エグゼクティブサマリ

VW は CARIAD（自社子会社）の VW.OS が迷走し、中国は XPeng（VLA 2.0 + CEA アーキテクチャ + 充電ネット共同）に依存転換、欧州は Cerence Chat Pro（OpenAI API）で当面凌ぐ。中国利益45%減（$2B → $1.1B）が外部依存深化の背景。ID.Unyx 08（VW×XPeng 第1号、$33,300〜、2026.4 量産）は L4 相当・地図不要を訴求。Honda にとって「自前OS開発の難しさ」を可視化する事例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | ID.Unyx 08（VW×XPeng 第1号、$33,300〜、2026.4）[一次] |
| 量産時期 | XPeng VLA 2.0 量産 [未特定] / ID.Unyx 08 2026.4 [一次] |
| 対象国 | 中国（XPeng JV）+ 欧州（Cerence Chat Pro）[一次] |
| AI Agent搭載総台数 | [未特定] |
| FM Level | A（Cerence Chat Pro = OpenAI API、中国は XPeng VLM/XGPT）|
| 主要採用FM | Cerence Chat Pro（OpenAI API）+ 中国向け XPeng VLM/XGPT [一次] |
| 採用Orchestrator | Cerence xUI（NVIDIA AI Enterprise + Azure）+ XPeng（China）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆 EV/PHV（VW/Audi/SEAT/Cupra）[一次]
- 旗艦モデルの市場定位：ID.Unyx 08 が中国専用、欧州は ID.Polo に Cerence xUI 展開
- 量産時期と地域戦略：中国 = XPeng JV、欧州 = Cerence Chat Pro/xUI 二極構造 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | エンタメ会話 + ナビ（中国は Tongxue 系より厚いが詳細[未特定]）|
| 体験の深さ | 中国 L4 相当（VLA 2.0 経由）/ 欧州 表層対話 [推論] |
| 個別最適化度 | [未特定] |

UXシナリオ要約：
中国専用 ID.Unyx 08 で XPeng VLA 2.0 採用、地図不要 L4 相当。欧州 ID.Polo は Cerence xUI で表層対話 [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3→C hybrid（中国は XPeng 依存、欧州は Cerence 依存）、Multi-Agent 空欄（Cerence Chat Pro 単一現行）[一次]
- 分類根拠：CARIAD 失速で外部依存（XPeng + Cerence）への完全シフト [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（OpenAI / XPeng VLM API利用）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Cerence Chat Pro（OpenAI API）+ 中国向け XPeng VLM/XGPT [一次] |
| 採用Orchestrator | Cerence xUI（NVIDIA AI Enterprise + Azure）+ XPeng（China）[一次] |
| 採用ミドルウェア（IVI OS）| CARIAD VW.OS（迷走→外部依存転換）[一次]/E/E は XPeng と共同開発 |
| 採用チップ（SoC）| [未特定]（Mobileye Chauffeur 採用）+ XPeng Turing（中国）[一次] |
| R&D投資規模（AI関連年額）| CARIAD 失速→外部依存（中国利益45%減 $2B→$1.1B）[一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | OpenAI（Cerence経由）+ XPeng（中国）|
| Orchestrator提供 | Cerence xUI + XPeng（中国）|
| Chip提供 | Mobileye + XPeng Turing |
| データ・地図提供 | [未特定] |
| ADAS提供 | Mobileye Chauffeur + XPeng VLA 2.0（中国）[一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（Cerence Chat Pro 2024.9〜 MY25）|
| a-2 ナビ・ルート | 実装済 |
| a-3 コックピット制御 | 部分実装（CARIAD VW.OS）|
| a-4 乗員ケア | 無 |
| a-5 コマース | [未特定] |

- 2027予測：P3-E（CEA 2.0 でcockpit-driving統合 agentic AI）
- 2030予測：P3-E or C 完全外部化

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 自社OS（CARIAD VW.OS）開発失敗が外部依存深化を招く実例。Honda の ASIMO OS が同じ轍を踏まないための規律として参照
- XPeng VLA 2.0 を欧州 OEM が採用する量産事例。中国AI の西側量産車搭載が現実化

### 6.2 警鐘 or 注意点
- 中国利益45%減（$2B → $1.1B）が外部依存を強いる。Honda が中国市場で同様の収益悪化に陥れば XPeng/Momenta 等への依存度が上昇する圧力

### 6.3 Honda の現在地との差分
Honda P2-T（ASIMO OS 自前堅持）と VW P3→C hybrid（CARIAD 失速）の差は明確。Honda は ASIMO OS の量産投入で VW の轍を回避する戦略規律が問われる。

---

## 7. [未特定] 残課題

- VW × XPeng VLA 2.0 量産年（理由：「第1顧客確定」のみ、量産投入年は非公表）→ 2026.3.2 launch 確定
- CARIAD VW.OS の今後の役割（理由：迷走の終着点未公開）→ パートナーソフト統合役（Rivian + XPeng）に縮退
- 欧州 Cerence Chat Pro の Agent 機能拡張ロードマップ（理由：[未特定]）

## 8. 2026 Q1-Q2 追加ファクト

- **CEA 量産開始（2026.1.29）：** ID.UNYX 08（中国専用、初の中国向け full-connected EV SUV）が量産入り、24ヶ月で series production 達成 [一次]
- 2026年 CEA で5新型 launch 計画 [一次]
- **XPeng VLA 2.0 を VW が初顧客（2026.3.2 launch）：** 中国EV メーカーの core AI 技術を Western OEM が大規模採用する初事例。L4 entry-level 自動運転対応、HDマップ不要 [一次]
- VW は XPeng L4 ソフトを license する **最初の Global OEM** [二次]
- CARIAD 戦略再定義：scratch から開発するのではなく、partner software（Rivian / XPeng）を integrate / coordinate する役割に縮退 [二次]
- 2026 通期で 20+ NEV 新型 launch 計画（"Delivery Mode" 継続）[一次]

## 出典（2026 Q1追加）

- [Carnewschina — VW starts production of XPeng co-developed CEA architecture](https://carnewschina.com/2026/01/29/volkswagen-starts-production-of-xpeng-co-developed-cea-architecture-five-new-models-due-in-2026/) [二次]
- [Technode — Volkswagen becomes launch customer for XPeng's VLA 2.0](https://technode.com/2026/02/26/volkswagen-becomes-launch-customer-for-xpengs-vla-2-0-model/) [二次]
- [CnEVPost — Xpeng secures VW as first customer for VLA 2.0](https://cnevpost.com/2026/02/24/xpeng-secures-vw-first-customer-vla-2-targets-1-million-overseas-sales-2030/) [二次]


## 直近アップデート
- 2026-05-11: CARIADの役割縮小を発表。RivianとXPengからソフトウェア調達へ転換。 ([出典](https://ev.com/news/volkswagen-scales-back-cariads-role-turns-to-rivian-and-xpeng-for-software-development))

### 2026-05-13
- 事実：VW-RivianのJVが自社EV/ソフトウェア技術を他社OEMへ売却することを検討
- 出典：https://www.autonews.com/volkswagen/ane-vw-rivian-ev-technology-1114/
- 発表日：（2025-11-14）
- 確度：中（industry_media）
- 2026-07-14: VW CEO Oliver Blume、ボード刷新計画可決できず。Audi/Porscheモデルカット検討。[AutoNews 2026-07] ([出典](https://eletric-vehicles.com/rivian/volkswagen-forms-task-force-as-rivian-software-alliance-falls-short-report/))
