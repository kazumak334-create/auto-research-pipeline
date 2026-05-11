# PEST分析: グローバルマクロ経済
**フレーム:** マンキュー経済学（マクロ）変数体系  
**最終更新:** 初版（2026-05-11）  
**更新者:** auto-agent

---

## 概要・主要論点

グローバルマクロをマンキュー経済学の変数体系（GDP・インフレ・金利・為替・貿易・雇用・生産性・マネーサプライ）で継続モニタリングする。
産業別PEST分析の「E軸」共通基盤として機能する。

**2026年5月時点のベースライン（最新データ）:**

| マンキュー変数 | 水準 | 方向感 |
|-------------|------|--------|
| 世界GDP成長率 | +3.3% | 横ばい（下方リスク：米関税） |
| 米国GDP成長率 | +2.6% | 減速傾向 |
| 中国GDP成長率 | +4.8% | 目標割れリスク |
| ユーロ圏GDP成長率 | +1.1% | 低空飛行 |
| 日本GDP成長率 | +0.6% | 円高・実質賃金回復待ち |
| 米国コアPCE | 2.6%（年末見通し） | 粘着性あり |
| Fed政策金利 | 3.0-3.25%（年末予想） | 利下げサイクル継続 |
| ECB政策金利 | 約2.0% | 据え置き～追加利下げ検討 |
| 日銀政策金利 | 0.5%→1.0%（7月予想） | 利上げサイクル継続 |

---

## P: 政治・通商政策 (Political)

### 主要監視テーマ
- 米国関税政策：自動車25% / 鉄鋼25% / 半導体 / 一般輸入品10%ベースライン
- 米中通商交渉の進捗（90日停戦延長 vs 永続化 vs 破断）
- G7/G20の経済安全保障アジェンダ（半導体・AI・バッテリー）
- EU競争力アジェンダ（Draghi報告書実装進捗）
- 途上国債務問題（対中デット・トラップ再燃リスク）

### 検索クエリテンプレート（{YYYY-MM}を当日年月に置換）
```
US tariff trade policy update {YYYY-MM} site:reuters.com OR site:ft.com
US China trade war tariff negotiation {YYYY-MM}
G7 economic security semiconductor AI {YYYY-MM}
EU competitiveness Draghi agenda implementation {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: Big Tech AI Capex ~$700B（MS+Google+Meta+Amazon）。銅2026年供給不足15万t、JPMorgan $12,500/t予測。リチウム価格+50% YTD。DeepSeek V4 MIT Licenseで価格破壊継続。中国NEV60.6%浸透で新エネ転換加速。米国関税でHonda $9.1B負担、USMCA再交渉7月。

---

## E: 経済・マクロ変数 (Economic) ※マンキュー体系

### GDP / 景気循環
**監視ポイント:**
- 米国ISM製造業PMI・サービスPMI（50割れで後退シグナル）
- 中国製造業PMI・社会消費品小売総額
- ユーロ圏GDP速報値・財政赤字/GDP比
- 日本実質賃金・個人消費

**検索クエリ:**
```
US GDP PMI economic outlook {YYYY-MM} site:reuters.com
China GDP growth consumer spending {YYYY-MM}
Eurozone GDP inflation recession risk {YYYY-MM}
Japan GDP real wages BOJ {YYYY-MM}
```

### インフレ・金融政策（マンキュー: 貨幣数量説・フィッシャー効果）
**監視ポイント:**
- 米国CPI/PCE月次→コアサービスインフレ粘着性
- Fed FOMC声明・ドット・プロット更新
- 日銀政策変更タイミング（実質金利 vs 名目賃金）
- 欧州エネルギー価格→コストプッシュインフレ再燃

**検索クエリ:**
```
Fed FOMC interest rate decision {YYYY-MM} site:federalreserve.gov OR site:reuters.com
US CPI PCE inflation {YYYY-MM}
BOJ interest rate hike decision {YYYY-MM} site:boj.or.jp OR site:reuters.com
ECB rate decision inflation {YYYY-MM}
```

### 為替・国際収支（マンキュー: 購買力平価・金利平価）
**監視ポイント:**
- USD/JPY（日銀利上げ×Fed利下げの同時進行）
- USD/CNY（人民元管理レート vs 市場実勢）
- 米国経常赤字/貿易赤字（関税効果の検証）
- 日本輸出企業の為替感応度（1円/ドル変動 = 営業利益XXX億円）

**検索クエリ:**
```
USD JPY exchange rate yen BOJ Fed {YYYY-MM}
China yuan CNY exchange rate trade {YYYY-MM}
US trade deficit current account {YYYY-MM}
```

### 投資・生産性（マンキュー: ソロー成長モデル）
**監視ポイント:**
- 米国設備投資（AI/半導体インフラ主導）
- 中国固定資産投資（過剰投資 vs 需要不足）
- 全要素生産性（TFP）に対するAI貢献度測定
- インフラ投資乗数（財政刺激の実効性）

**検索クエリ:**
```
AI productivity growth investment GDP {YYYY-MM} OECD IMF
China fixed asset investment overcapacity {YYYY-MM}
US capital investment AI infrastructure {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## S: 社会・人口動態 (Social)

### 主要監視テーマ
- 少子高齢化：日本・中国・欧州の生産年齢人口減少速度
- 労働市場：米国非農業部門雇用・失業率（NAIRU との乖離）
- 所得格差：ジニ係数変化・中間層の購買力
- 人口流入：移民政策変化（米国 vs EU vs 日本）
- 生成AIによる労働代替：ホワイトカラー職への影響

### 検索クエリテンプレート
```
global demographics aging population productivity {YYYY-MM}
US labor market employment unemployment NAIRU {YYYY-MM}
income inequality middle class consumption {YYYY-MM}
AI job displacement white collar labor market {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## T: 技術・イノベーション (Technological)

### 主要監視テーマ
- AI：大規模言語モデル能力向上速度（GPT-5 / Gemini Ultra / Claude 4系）
- 半導体：3nm/2nm量産移行タイムライン・AI特化チップ設計
- エネルギー転換：バッテリーコスト曲線・洋上風力コスト
- 量子コンピューティング：実用化ロードマップ（2030目標）
- バイオテクノロジー：CRISPR 応用・mRNA医薬品産業化

### 検索クエリテンプレート
```
AI frontier model GPT Gemini Claude benchmark {YYYY-MM}
semiconductor 2nm 3nm TSMC production {YYYY-MM}
battery cost kWh energy transition {YYYY-MM}
quantum computing milestone roadmap {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## 産業横断リスクシナリオ

| シナリオ | 確率（主観） | 産業別インパクト |
|---------|-----------|---------------|
| 米中貿易戦争エスカレーション（関税60%以上） | 25% | 自動車・半導体・資源に高インパクト |
| 米国景気後退（2027年以内） | 30% | AI投資一時後退・自動車販売減少 |
| 日本急激な円高（1ドル=120円台） | 20% | 製造業輸出利益圧迫 |
| 中国デフレーション輸出の深刻化 | 40% | 全産業で価格競争激化 |
| AI生産性革命が早期到来（GDP+0.5%上乗せ） | 15% | ポジティブ・テクノロジー各社恩恵 |

---

## 更新ログ

| 日付 | 更新内容 | 更新者 |
|------|---------|--------|
| 2026-05-11 | 初版作成。マンキュー変数体系・2026年5月ベースライン設定 | auto-agent |
