# PEST分析: 自動車産業
**フレーム:** PEST × CASE-X（EV転換・SDV・地政学）  
**最終更新:** 初版（2026-05-11）  
**更新者:** auto-agent  
**注:** `macro-industry.md`（Honda固有分析）と連携して読む

---

## 概要・主要論点

自動車産業はEV転換・SDV化・中国勢台頭・米関税という4重変化が同時進行中。
CASE（Connected / Autonomous / Shared / Electric）× 地政学リスクがバリューチェーン全体を再編する。

**2026年5月時点のキーナンバー:**

| 指標 | 数値 | ソース |
|------|------|--------|
| 世界EV販売シェア | ~20%（2025年推計） | BNEF |
| 中国NEV月次販売 | 約120万台/月 | CPCA |
| BYD四輪世界販売 | 約180万台/年 | BYD |
| 米国自動車輸入関税 | 25% | 米国政府 |
| EU対中EV相殺関税（SAIC） | 35.3% | EC |

---

## P: 政治・通商政策 (Political)

### 主要監視テーマ
- 米国自動車関税25%：Honda/Toyota北米生産移管進捗・USMCA適格化
- EU対中EV相殺関税（BYD 17% / Geely 18.8% / SAIC 35.3%）改定・WTO提訴動向
- EU CO2規制2035年見直し（ICE/HEV容認範囲の変化）
- 米国コネクテッド車両規制（中国製ソフト・ハードウェア禁止範囲）
- ASEAN各国ローカルコンテンツ要件（タイEV3.0/3.5後継政策）
- 中国NEVクレジット制度・補助金動向

### 検索クエリテンプレート（{YYYY-MM}を当日年月に置換）
```
US auto tariff 25% Honda Toyota USMCA {YYYY-MM} site:reuters.com OR site:ft.com
EU anti-subsidy tariff Chinese EV update {YYYY-MM}
EU CO2 regulation 2035 ICE ban HEV update {YYYY-MM}
US connected vehicle regulation China software ban {YYYY-MM}
ASEAN automotive local content EV policy {YYYY-MM}
China NEV credit subsidy policy {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## E: 経済 (Economic) ※マンキュー変数ベース

### マクロ変数→自動車産業への波及
| マンキュー変数 | 自動車産業への影響 |
|-------------|----------------|
| 金利（Fed 3.0-3.25%） | 自動車ローン金利高止まり→米国販売台数抑制 |
| 為替（円安傾向） | 日本OEM輸出競争力↑、ただし関税でオフセット |
| 中国GDP +4.8% | NEV需要は維持。価格戦争継続中 |
| 米国GDP +2.6%↓ | 高価格帯SUV需要鈍化リスク |

### 産業固有経済指標
**監視ポイント:**
- 主要OEM四半期営業利益率（Honda / Toyota / BYD / Tesla比較）
- 中国EV価格戦争：値引き幅・インセンティブ水準（平均ASP下落速度）
- バッテリーコスト（$/kWh）：LFP ~$70 / NMC ~$90（2026年1Q）
- 全固体電池量産投資額（Toyota 2027年vs BYD 2027-28年）
- 中国NEVクレジット市場価格

**検索クエリ:**
```
automotive earnings OEM profit margin Q{Q} 2026 Honda Toyota BYD
China EV price war discount incentive ASP {YYYY-MM}
battery cost kWh LFP NMC trend 2026
solid state battery investment Toyota BYD {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## S: 社会・消費者行動 (Social)

### 主要監視テーマ
- 中国消費者：EV購買決定因子変化（価格 vs 技術 vs ブランド）
- EV再購入意向率・ICE回帰率（欧州・北米・ASEAN）
- ASEAN各国の中国ブランド受容度（日系ブランド好感度対比）
- 欧州における中国製EV購入意向と安全性懸念
- 自動車所有から移動サービス利用へのシフト速度（都市部）

### 横比較表（月次更新）

| 市場 | 最新月 | BYD | Geely/Zeekr | NIO/ONVO | Li Auto | Honda | Toyota | 備考 |
|------|--------|-----|-------------|----------|---------|-------|--------|------|
| 中国NEV（万台） | - | - | - | - | - | - | - | |
| タイ（全体） | - | - | - | - | - | - | - | |
| インドネシア（全体） | - | - | - | - | - | - | - | |

### 検索クエリテンプレート
```
consumer survey EV brand preference China {YYYY-MM}
ASEAN Chinese car brand consumer attitude {YYYY-MM}
EV adoption survey Europe North America {YYYY-MM}
China NEV monthly sales BYD {YYYY-MM} site:carnewschina.com OR site:cnevpost.com
Thailand Indonesia EV market share {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## T: 技術 (Technological)

### 主要監視テーマ
- バッテリー：全固体電池量産マイルストーン / LFP充電速度向上（4C→6C）
- SDV：OTA更新頻度格差（中国勢2週間 vs 日系3-6ヶ月）縮小速度
- 充電規格：GB/T vs CCS 各国採用状況（ASEAN標準化議論）
- 自動運転：L3量産（メルセデス・Honda）/ L4ロボタクシー（Baidu / Waymo）
- Huawei HIMA：参加OEM数・Ascend AI チップ性能向上
- 車両アーキテクチャ：BEV専用プラットフォーム vs マルチパワートレイン共用

### 検索クエリテンプレート
```
solid state battery mass production timeline 2026 Toyota BYD
EV battery cost kWh trend {YYYY-MM}
OTA update automotive SDV China Japan {YYYY-MM}
autonomous driving L3 L4 robotaxi {YYYY-MM}
Huawei HIMA automotive chip {YYYY-MM}
charging standard ASEAN GB/T CCS {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## Honda固有リスクサマリー（マクロ→Honda連鎖）

| マクロリスク | Honda固有インパクト | KPI |
|-----------|------------------|-----|
| 米国関税25%継続 | 北米工場移転コスト・Honda Car Canada閉鎖検討 | USMCA適格比率 |
| 中国NEV価格戦争 | GAC-Honda / DH合弁収益消滅リスク | 合弁工場稼働率 |
| ASEAN中国EV攻勢 | タイ・インドネシアシェア喪失加速 | 月次販売比較 |
| 日銀利上げ→円高 | 輸出採算ライン悪化（管理レート：当期?) | 為替感応度 |

---

## 更新ログ

| 日付 | 更新内容 | 更新者 |
|------|---------|--------|
| 2026-05-11 | 初版作成。PEST × CASE-Xフレーム統合。macro-industry.mdのHonda固有軸は別ファイルに保持 | auto-agent |
