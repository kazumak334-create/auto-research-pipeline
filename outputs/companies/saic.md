# SAIC — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-T（DeepSeek + Qwen + Horizon・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ 2026 H1 新型 matrix 投入：IM LS9 Hyper / IM LS8 / SAIC Audi E7X。**Q1 2026 SAIC Audi 端末販売 10,000台超 +28% YoY**。**Audi-SAIC 戦略合作 拡大（2026.4.17 調印）**：Shanghai に Audi Innovation Technology Center 設立、ICV / 知能電動 全車開発フォーカス。Audi E7X（初 SUV）2026 北京モーターショーでdebut、3rd model 2027
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ ChinaEVHome + SAIC 公式

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | SAIC-GM JV（DeepSeek R1初統合）/ IM Motors（自社EV）[一次] |
| 量産時期 | DeepSeek 2025〜、Qwen 2026 [一次] |
| 対象国 | 中国 + 海外 [一次] |
| AI Agent搭載総台数 | 多 JV / IM Motors 全車 [推論] |
| FM Level | A（DeepSeek + Qwen API利用）|
| 主要採用FM | DeepSeek + Qwen（2026.4 北京）[一次] |
| 採用Orchestrator | IM Motors 自前 + JV 各社 [一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-T、Multi-Agent 空欄
- FM Level：A（外部API、多FM 並走）
- 採用チップ：Horizon Journey 6（中国製）[一次]
- SAIC-GM JV は DeepSeek R1 初統合（2025.2 一斉統合 10社の一角）[一次]

---

## 6. Honda 示唆（So What）

SAIC は中国合弁の代表（GM/VW）+ IM Motors 自社EV の二段構造。Honda の中国合弁（広汽/東風）との競合関係で、SAIC が DeepSeek + Qwen で自社路線を強化する動きは Honda 合弁戦略の脅威。Qwen 採用は Alibaba エコシステム連結（コマース・地図）への扉。**Audi-SAIC 戦略合作 拡大（2026.4.17）= Shanghai Audi Innovation Center 設立で Audi が中国EV 開発を SAIC に大幅依存** = Honda が中国合弁の知能電動 R&D を本田技研本体から SAIC型現地依存型に切替えるか否かの分岐参照。

## 7. 2026 Q1-Q2 追加ファクト

- 2026 H1 新型 matrix：IM LS9 Hyper / IM LS8 / SAIC Audi E7X 投入計画 [二次]
- **Q1 2026 SAIC Audi 端末販売 10,000台超 +28% YoY** [二次]
- **2026.4.17 Audi-SAIC 戦略合作 新ラウンド調印**：Shanghai に Audi Innovation Technology Center 設立、smart electrification + ICV 全車開発フォーカス [二次]
- Audi E7X（初 SUV）が 2026 北京モーターショー debut、3rd model は 2027 launch 予定 [二次]
- IM Motors（SAIC + Alibaba + Zhangjiang Hi-Tech のJV）：global strategy で 2024年から多市場進出、2025-2026 拡大継続 [二次]

## 出典（2026 Q1追加）

- [SAIC 公式 — SAIC Motor's Jan-Feb sales](https://www.saicmotor.com/english/latest_news/saic_motor/63921.shtml) [一次]
- [ChinaEVHome — Audi, SAIC Set Up Innovation Center in China](https://chinaevhome.com/2026/04/17/audi-saic-set-up-innovation-center-in-china-to-develop-next-gen-audi-models/) [二次]
- [Automotive World — Audi and SAIC deepen ties with four new models](https://www.automotiveworld.com/news/audi-and-saic-deepen-ties-with-four-new-models-rd-hub/) [二次]


## 直近アップデート
- 2026-05-11: IM Motors LS8 EREV SUV発売、36,600ドルから、EV航続430km。 ([出典](https://carnewschina.com/2026/04/17/im-motors-launches-ls8-erev-suv-starting-from-36600-usd-430-km-ev-range-and-four-wheel-steer-by-wire/))

### 2026-05-13
- 事実：SAIC MG がMG 07セダンをティザー公開。ルーフ搭載LiDAR初採用（MG初）、価格帯15〜20万元、年内発売予定
- 出典：https://cnevpost.com/2026/05/09/saic-mg-teases-mg-07-sedan/
- 発表日：2026-05-09
- 確度：中（industry_media）
