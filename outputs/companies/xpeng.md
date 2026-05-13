# XPeng — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P1-E（垂直完全・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **VW を VLA 2.0 初顧客に確定**（2026.3.2 launch、中国EV メーカーの core AI を Western OEM 大規模採用初事例）。2026 通期目標 550-600K台、Q1 2026 ガイダンス 61-66K（YoY -30〜-35%、税優遇縮小・季節要因）。Robotaxi BU 新設（L4 driverless 2027目標）。海外2030目標 100万台
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CnEVPost + Technode + CNBC

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | GX（750km L4-ready, $58K, 2026.4 北京モーターショー）[一次] |
| 量産時期 | VLA 2.0 量産中、X9 2026 [一次] |
| 対象国 | 中国 + VW向け技術輸出 [一次] |
| AI Agent搭載総台数 | VW ID.Unyx 08 含む技術輸出展開 [推論] |
| FM Level | C（自社 VLA 2.0 + XGPT + Turing チップ）|
| 主要採用FM | XPeng VLM/XGPT（自社）+ VLA 2.0 [一次] |
| 採用Orchestrator | XMARTOS + General Intelligence Center（2026.2 設立）[一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P1-E、Multi-Agent ◎（VLA 2.0 + General Intelligence Center 統合）
- FM Level：C（Full Stack型）
- 採用チップ：XPeng Turing（750 TOPS、30Bパラメータローカル推論、2025年G7初搭載）[一次]
- R&D投資：2025 RMB 8.5B + Turing 1500+TOPS [一次]

---

## 6. Honda 示唆（So What）

XPeng VLA 2.0 が VW CEA アーキテクチャに採用される量産事例は「中国AI の西側量産車搭載」の象徴。**2026.3.2 VW launch customer 確定により、XPeng は中国EV メーカーで初めて core AI 技術を Global OEM に license する立場を確立**。Honda が中国向け Momenta 採用と同様、XPeng 採用の選択肢も視野に入れるべき。General Intelligence Center（2026.2 設立）は cockpit + driving 統合 Orchestration の最先端事例。

## 7. 2026 Q1-Q2 追加ファクト

- **VW が VLA 2.0 初顧客（2026.3.2 launch）：** 中国EV メーカー → Global Tier-1 OEM への core AI 大規模ライセンス 初事例 [一次]
- VLA 2.0 は entry-level L4 対応、HD マップ不要、狭路・campus シーン カバー [二次]
- 2026 通期目標 550-600K台、Q1 2026 ガイダンス 61-66K（YoY -30〜-35%、税優遇縮小・季節要因）[二次]
- 海外販売 2026 倍増、2030 100万台目標 [一次]
- 海外利益寄与 2030 70%超目標 [一次]
- Robotaxi BU 新設、L4 driverless 2027 商業運用目標 [二次]

## 出典（2026 Q1追加）

- [CnEVPost — Xpeng secures VW as first customer for VLA 2.0](https://cnevpost.com/2026/02/24/xpeng-secures-vw-first-customer-vla-2-targets-1-million-overseas-sales-2030/) [二次]
- [Technode — Volkswagen becomes launch customer for XPeng's VLA 2.0](https://technode.com/2026/02/26/volkswagen-becomes-launch-customer-for-xpengs-vla-2-0-model/) [二次]
- [CNBC — VW deal with XPeng shows how China tech threatens Western automakers](https://www.cnbc.com/2026/04/01/volkswagen-xpeng-deal-threat-rivian-us-automakers.html) [二次]


## 直近アップデート
- 2026-05-11: Volkswagen が XPeng VLA 2.0 自律走行ソリューション採用を発表。4月販売31,011台 (-11.5% YoY)。 ([出典](https://eletric-vehicles.com/xpeng/volkswagen-to-adopt-xpengs-autonomous-driving-solution-vla-2-0/))

### 2026-05-13
- 事実：XPeng VLA 2.0 自律走行テストドライブ報告。TeslaのFSD独占に並ぶ実力と評価。MagnaオーストリアでXPeng/BYDが欧州現地生産
- 出典：https://electrek.co/2026/04/29/xpeng-vla-2-test-drive-tesla-not-alone-full-self-driving/
- 発表日：2026-04-29
- 確度：中（industry_media）
