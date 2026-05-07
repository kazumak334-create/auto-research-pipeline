# InCar / OutCar / Cloud レイヤー分解｜テーマ別リサーチノート

## 1. テーマ概要

**論点:** 自動車産業の競争軸を InCar / OutCar / 周辺IT / Cloud / Data の5レイヤーに分解し、各プレイヤーがどの層で競争優位を築いているかを整理する。

---

## 2. レイヤー定義

| レイヤー | 内容 |
|---|---|
| InCar | コックピット、ADAS、E/Eアーキテクチャ、センサー、HMI |
| OutCar | スマートフォン連携、周辺デバイス、充電インフラ |
| 周辺IT | 地図、決済、メディア、コンテンツ配信 |
| Cloud | OTA管理、フリート管理、V2X、AI学習基盤 |
| Data | 走行データ、利用ログ、車両状態データ |

---

## 3. プレイヤー × レイヤーマップ

| プレイヤー | InCar | OutCar | 周辺IT | Cloud | Data |
|---|---|---|---|---|---|
| Huawei | ◎（ADS・HarmonyOS） | ○（スマホ連携） | △ | ○ | ○ |
| Xiaomi | ◎（HyperOS） | ◎（スマホ統合） | ○ | ○ | ○ |
| BYD | ◎（DiLink・DiPilot） | △ | △ | △ | ◎（自社） |
| Baidu | ○（Apollo） | × | ◎（地図） | ◎ | ◎ |
| Tencent | ○（TAI） | ○（WeChat） | ◎（決済・SNS） | ◎ | ○ |
| Alibaba | ○（AliOS） | ○（Alipay） | ◎（EC・決済） | ◎ | ○ |
| ByteDance | △ | ○（TikTok） | ◎（コンテンツ） | ○ | △ |
| Toyota | ○（Safety Sense） | △ | × | △（Woven） | △ |

凡例: ◎強い競争優位 ○参入済み △限定的 ×未参入・低存在感

---

## 4. 競争が激化しているレイヤー

1. **InCar（コックピットOS）**: HarmonyOS・AliOS・HyperOSが競合。OEMの自社OS開発が急務。
2. **Cloud（AI学習基盤）**: Baidu・Alibaba・Tencentが先行。OEMのAI競争力に直結。
3. **Data**: 走行データの帰属が未解決のまま各プレイヤーが収集中。

---

## 5. トヨタ・OEMへの示唆

- InCarとCloudの両方で弱いOEMは「ハードウェア製造業」に収縮するリスクが高い。
- WovenがCloud・Data層をカバーできるかが、トヨタのSDV戦略の成否を左右する。

---

## 6. 追加調査ToDo

- [ ] 各プレイヤーのCloud売上に占めるAutomotive比率（公式IR確認）
- [ ] InCar OS競争のシェアデータ（中国市場）
- [ ] Woven Toyota の事業進捗（2025年以降の公式発表）

---

## 7. 更新ログ

| 日付 | 更新内容 | 更新者 |
|---|---|---|
| 2026-05-07 | 初期テンプレート作成 | system |
