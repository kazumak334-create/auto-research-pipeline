# Leapmotor — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-T（DeepSeek + Stellantis資本・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Q1 2026 欧州納車 24,751台（+706% YoY）**：12 EU 国 純EV 17K台で中国EV ブランド首位。**イタリア純EV 33.5%シェア**（小売 44.6%）、ドイツ Q1 3,168台 +370.7%。世界 40+ 市場、950 outlet 確立。3月単月 50,029台、Brussels Motor Show で B03X / B05 / B10 Hybrid EV 発表
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Stellantis Media（2026.4）

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | C16 / B10 系（Stellantis販売網経由 海外）[一次] |
| 量産時期 | DeepSeek 統合中 [一次] |
| 対象国 | 中国 + 欧州（Stellantis経由）[一次] |
| AI Agent搭載総台数 | 596,555台（2025、初年度黒字 RMB 540M）[一次] |
| FM Level | A（DeepSeek API利用）|
| 主要採用FM | DeepSeek [一次] |
| 採用Orchestrator | [未特定] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-T、Multi-Agent 空欄
- FM Level：A（外部API利用）
- Stellantis 資本提携で欧州販売網アクセス、海外展開ルート確保

---

## 6. Honda 示唆（So What）

Leapmotor は中国OEM が西側資本（Stellantis）で海外展開する事例。Honda が中国市場で逆方向（中国OEM との資本・技術提携）を取る選択肢の参照。**Q1 2026 欧州納車 +706% YoY、イタリア純EV 33.5%シェア = 中国EV の欧州侵食ペースが Honda 想定を超えて加速**。Honda 欧州EV 戦略の競合圧力を定量化する重要指標。

## 7. 2026 Q1-Q2 追加ファクト

- **Q1 2026 欧州納車 24,751台（+706% YoY、+39% QoQ）**[一次]
- 16 欧州国合計 23,300台（+726.5% YoY）、12 EU 国 純EV 17K台で中国EV ブランド首位 [一次]
- イタリア純EV シェア 33.5%（小売 44.6%）、ドイツ Q1 3,168台（+370.7% YoY）、3月単月で 10,000台目納車達成 [一次]
- 全社3月単月 50,029台 [一次]
- 40+ 国際市場展開、950 海外 outlet [一次]
- Brussels Motor Show 2026 で B03X 欧州 premiere、B05 内装公開、B10 Hybrid EV launch [一次]
- Stellantis 51% / Leapmotor 49% の Leapmotor International（2024年設立）が中国外販売を担当 [一次]

## 出典（2026 Q1追加）

- [Stellantis Media — Leapmotor March 2026 Results in Europe](https://www.media.stellantis.com/em-en/leapmotor/press/leapmotor-march-2026-results-in-europe) [一次]
- [Stellantis Media — Leapmotor Q1 No.1 NEV Start Up](https://www.media.stellantis.com/em-en/leapmotor/press/leapmotor-confirms-no-1-nev-start-up-position-with-robust-q1-growth-and-50-029-vehicles-in-march-2026) [一次]


## 直近アップデート
- 2026-05-11: Stellantisとのパートナーシップ拡大、欧州EV製造推進。4月71,387台 (+73.9%) 過去最高。 ([出典](https://www.cbtnews.com/stellantis-leapmotor-expand-partnership/))

### 2026-05-13
- 事実：StellantisとLeapmotorがスペインで共同生産を決定。B10 SUVとOpelブランドの新型EV C-SUVをZaragoza工場で製造（EU関税回避）
- 出典：https://www.detroitnews.com/story/business/autos/chrysler/2026/05/08/stellantis-leapmotor-deepen-ties-with-joint-ev-production-in-europe/89999473007/
- 発表日：（2026-05-08）
- 確度：中（industry_media）
- 2026-07-14: 中国NEV市場3位に急浮上（6月72,376台、7.2%シェア）。H1: 260,193台（10位→3位の大幅上昇）。[CPCA 2026-07-10] ([出典](https://insideevs.com/news/800900/leapmotor-mexico-sales-stellantis-chinese/))
