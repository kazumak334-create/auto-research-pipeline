# Ford — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3-T（Google Cloud・移行中）→ EV 大幅縮退で再評価
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **EV 戦略大幅後退**：F-150 Lightning EV 中止→Hybrid化、$19.5B EV 計画再構築コスト計上。**EV 統括 Doug Field 退社（2026.4）**。BlueOval SK 解消（Q1 2026）。HEV/EREV/低価格車・F1 技術・Energy storage（Ford Energy 20GWh by 2027）にシフト。EV部門の利益化目標 = 2029
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CNBC（2026.4.15）+ Eletric-vehicles + WardsAuto

---

## 1. エグゼクティブサマリ

Ford は CES 2026 で AI アシスタントを発表（Google Cloud ホスト、オフザシェルフLLM 使用）。Ford アプリ経由で2026年初頭、車内搭載は2027年と段階的展開。**ただし 2026 Q1 で EV 戦略を大幅縮退**：F-150 Lightning EV 中止（Hybrid 化）、$19.5B 規模の EV プログラム書込み、BlueOval SK 解消（2026 Q1）、EV 統括 Doug Field 退社（2026.4）。HEV/EREV/低価格車・F1 技術・Energy storage（Ford Energy）に re-allocation。EV 部門の利益化目標は 2029 に後ろ倒し。Honda 0 SUV 中止と同種の「米国EV撤退」連鎖の代表例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | F-Series（米国 828K台）+ AI Assistant 全車対応 [一次] |
| 量産時期 | App 2026 / 車内 2027 [一次] |
| 対象国 | 北米中心 [一次] |
| AI Agent搭載総台数 | F-Series 全車 + Ford アプリ ユーザー [推論] |
| FM Level | A（Google Cloud、FM種別非公開）|
| 主要採用FM | Google Cloud（FM種別非公開）[一次] |
| 採用Orchestrator | Google Cloud（外部ホスト）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆 + ピックアップ（F-Series）[一次]
- 旗艦モデルの市場定位：F-Series 米国 828K台、AI Assistant 全車対応
- 量産時期と地域戦略：北米先行、App→車内の段階的展開 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事（CES 2026 発表）[一次] |
| 体験の深さ | Tool Use（車両固有情報・リアルタイム車両状態アクセス）[一次] |
| 個別最適化度 | [未特定] |

UXシナリオ要約：
スマホアプリで先行、車内2027 で deep integration [一次]。車両固有情報・リアルタイム車両状態アクセスを訴求。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-T、Multi-Agent 空欄（Google 単一）[一次]
- 分類根拠：Google Cloud 完全外部ホスト、Orchestrator も Google [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用、Google Cloud LLM）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Google Cloud（FM種別非公開）[一次] |
| 採用Orchestrator | Google Cloud（外部ホスト）[一次] |
| 採用ミドルウェア（IVI OS）| Ford Sync（次世代）[推論] |
| 採用チップ（SoC）| [未特定] |
| R&D投資規模（AI関連年額）| [未特定] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Google Cloud |
| Orchestrator提供 | Google Cloud |
| Chip提供 | [未特定] |
| データ・地図提供 | Google Maps |
| ADAS提供 | BlueCruise（自前、Lvl 2+, 264M miles +88%）[一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 2026（App）/2027（車内）|
| a-2 ナビ・ルート | 実装済（Sync）|
| a-3 コックピット制御 | 部分実装（BlueCruise 264M miles +88%）|
| a-4 乗員ケア | 無 |
| a-5 コマース | 2027（車内連携後）|

- 2027予測：P3-E（次世代BlueCruise + 車内 AI Assistant）
- 2030予測：P3-E（eyes-off driving 2028 達成後）

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- Ford はApp→車内の段階展開で2027 までずれる慎重派。Honda 0 SUV 中止と Ford EV プログラム後退は **同じ「米国EV市場の経済合理性破綻」連鎖** の現れ
- 「外部FM 完全依存」の典型例。Honda が ASIMO OS で Orch 自前を堅持する戦略の正当性を補強

### 6.2 警鐘 or 注意点
- Ford は北米で F-Series の圧倒的シェアを背景に「EV 撤退してもキャッシュは確保」できる立場。Honda は同じ余裕がない（HEV シェアは Toyota に劣後）
- **EV 統括役員（Doug Field）退社（2026.4）** は「EV 戦略責任の不在」を示唆。Honda の SHM 縮退と同型の人事再編
- Ford Energy（電池工場 → エネルギー貯蔵 20GWh by 2027）への pivot は EV 投資の sunk cost を別事業で回収する手法。Honda の電池資産処遇の参照

### 6.3 Honda の現在地との差分
Honda 0 Series 中止（2026.3.12）と Ford EV プログラム後退（2026 Q1, $19.5B 計上）は同じ局面。Honda P2-T と Ford P3-T の差は Orch 内製度合いだが、両社とも「AI 戦略は事業戦略の従属変数」を示す事例。

---

## 7. [未特定] 残課題

- Ford 2026 App から 2027 車内 deep integration の機能差（理由：段階差の具体仕様未公開）
- Google Cloud 採用 LLM 種別（理由：[未特定]）
- 次世代 BlueCruise 30%コスト削減の達成手段（理由：[未特定]）
- Doug Field 後任の EV/SDV 統括人事
- $19.5B 計上後の AI/SDV 投資の継続可否

## 8. 2026 Q1-Q2 重大変更ファクト

- **F-150 Lightning EV 中止** → Hybrid 化（最大の犠牲）[二次]
- **$19.5B EV プログラム再構築コスト**（2025計上）。$10.7B impairment + 各種 write-down [二次]
- **BlueOval SK 電池JV 解消**（Q1 2026 中、SK On 公表）[二次]
- **EV 統括 Doug Field 退社（2026.4）**：5年弱のEV/SDV変革主導後、Product Creation 再編に伴い退任 [二次]
- Ford Energy 立上：Kentucky 電池工場を 20GWh advanced battery energy storage に転換（2027）[二次]
- EV 部門の利益化目標は **2029** に後ろ倒し [二次]
- CEO Jim Farley は留任、戦略再構築継続 [二次]

## 出典（2026 Q1追加）

- [CNBC — Ford EV leader Doug Field](https://www.cnbc.com/2026/04/15/ford-ev-leader-doug-field.html) [二次]
- [Eletric-vehicles — Ford Restructures EV Plans Again as Unit's Chief Exits](https://eletric-vehicles.com/ford/ford-restructures-ev-plans-again-as-units-chief-exits-farley-courts-china/) [二次]
- [WardsAuto — Ford scraps EV plans, shifts to hybrids, EREVs](https://www.wardsauto.com/news/ford-scraps-ev-plans-focusing-hybrids-erevs-new-trucks-battery-storage/808026/) [二次]
- [WardsAuto — Ford, SK On dissolving BlueOval SK](https://www.wardsauto.com/news/ford-skon-dissolving-blueoval-sk-ev-battery-joint-venture/807726/) [二次]
