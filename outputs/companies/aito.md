# AITO（Huawei HIMA） — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P1-T（Huawei 完全依存・移行中）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **AITO M6 = 24h で 60K受注、20日で 100K受注**（HIMA Spring Launch、2026.4.22 正式 launch、269.8K元〜）。Maextro S800 + AITO M9 が世界最高仕様 LiDAR で予約開始（2026.3.4）。HIMA 80+ モデル展開計画継続
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CnEVPost + GlobalChinaEV

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | M9 / M9L（次世代 6 LiDAR、Qiankun ADS 4.1→5.0）[一次] |
| 量産時期 | ADS 5.0 + HarmonySpace 6 = 2026.4 [一次] |
| 対象国 | 中国 [一次] |
| AI Agent搭載総台数 | HIMA 5社 + 2026 80モデル超 [一次] |
| FM Level | A（Huawei PanGu/Cangji 系、車両側は Huawei 提供）|
| 主要採用FM | Huawei 独自LLM（PanGu / Cangji 系）+ XiaoYi AI Agent [一次] |
| 採用Orchestrator | HMAF（HarmonyOS Multi-Agent Framework）[一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P1-T（OEM主導/Huawei Deep Engage 形式）、Multi-Agent ◎（Huawei XiaoYi + HMAF + ADS 5.0）
- FM Level：A（Huawei 提供FM 全依存）
- ADS 5.0 は V2V 車車間通信初搭載、L3 支援設計（規制待ち）
- HarmonyOS Cockpit 6 / HarmonySpace 6 で 80+ Agent Hub 経由

---

## 6. Honda 示唆（So What）

AITO は HIMA（Huawei Inside Mobility Alliance）参加で Huawei 完全依存型。Honda が中国市場で同等の依存戦略を取る場合の参照だが、データ主権・地政学リスクが大。「車両OEM が ADS + IVI を全外部委託する」極端パターンとして警鐘。**M6 受注 24h で 60K、20日で 100K** = Huawei ブランドへの中国市場の絶対的信頼。Honda 中国合弁モデルが対抗するには Huawei 提携 or 大幅技術差別化が必要。

## 7. 2026 Q1-Q2 追加ファクト

- **AITO M6 launch（2026.4.22）：** mid-large 5座 SUV、HIMA Spring Launch にて [一次]
- **24時間で 60K受注、20日で 100K受注**（2026.3.23 pre-sale 開始）[一次]
- 価格：269,800 元〜（約 $39,040）[一次]
- 1,000+ HIMA showroom に display unit 4月配備 [一次]
- Maextro S800 + AITO M9 pre-order 開始（2026.3.4）— 世界最高仕様 LiDAR 搭載 [二次]
- M5（229.8K元〜）と M7（309.8K元〜）の中間に位置づけ [一次]

## 出典（2026 Q1追加）

- [CnEVPost — Aito to launch new SUV M6 in Q2 2026](https://cnevpost.com/2025/11/24/aito-to-launch-new-suv-m6-q2-2026/) [二次]
- [GlobalChinaEV — AITO M6 60,000 pre-orders in 24 hours](https://www.globalchinaev.com/post/huawei-backed-aito-m6-arrives-in-showrooms-with-60000-pre-orders-in-24-hours) [二次]
- [CnEVPost — Huawei HIMA opens pre-orders for Maextro S800, Aito M9](https://cnevpost.com/2026/03/04/huawei-hima-opens-pre-orders-maextro-s800-aito-m9-top-spec-lidar/) [二次]


## 直近アップデート
- 2026-05-11: AITOがBMW・Mercedes-Benzと中国充電JVに対等パートナーとして参加。 ([出典](https://electrek.co/2026/04/22/seres-aito-joins-bmw-mercedes-ionchi-charging-jv-china/))

### 2026-05-13
- 事実：2026-05-13: 更新なし（本日取得JSONは空データ）
