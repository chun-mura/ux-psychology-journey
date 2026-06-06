## 概要

BJ Fogg の Behavior Model「B=MAP」（Behavior = Motivation × Ability × Prompt）を理解し、UIの摩擦・動機・トリガーの3軸で画面を分析できるようになる。

---

## 学習順序

### ステップ1：理論インプット（1時間）

[Stanford Behavior Design Lab](https://behaviordesign.stanford.edu/) のサイトで無料コンテンツを読む。

特に「Behavior Design Boot Camp」の概念説明部分が簡潔でわかりやすい。

3要素をこの順で理解する：

1. **Ability から先に理解する**：人は「できないから」行動しない、が最も多い原因
2. **Motivation はコントロールしにくい**：高低は波がある。だから Ability と Prompt に集中する
3. **Prompt はタイミングが命**：Motivation と Ability が揃った瞬間に届かないと無効

### ステップ2：Action Line を手書きで描く（20分）

縦軸を Motivation、横軸を Ability にした曲線グラフを描く。

「右下（Ability 高・Motivation 低）でも行動できる」ことを確認する。

自分がよく使うアプリの「最初の行動」をこの図に置いてみる。

### ステップ3：既存UIを3画面B=MAPで分析する（1.5時間）

Abilityを下げている摩擦を探すのが核心。以下の画面から選ぶ：

| 画面 | 見るべき摩擦 |
| --- | --- |
| 会員登録 | 入力項目数・パスワード要件・メール確認 |
| 課金誘導 | 価格の見せ方・リスク感・選択肢の多さ |
| 投稿フォーム | 文字数制限・ファイルサイズ・プレビュー有無 |

各画面を「Abilityの何を妨げているか（時間・認知・習慣）」で分類し、改善案を1つ出す。

### ステップ4：Hook Model（Issue #1）との違いをまとめる（30分）

- Fogg BM：**1回の行動を起こす**ための設計（新規獲得・コンバージョン）
- Hook Model：**繰り返し行動を定着させる**ための設計（リテンション・習慣化）
- 使い分け：LP/登録フローは Fogg BM、DAU向上は Hook Model

---

## やること

- [ ]  **B=MAP の3要素を整理する**
    - Motivation の6要素：快楽/苦痛、希望/恐怖、社会的受容/拒絶
    - Ability の6要素：時間・お金・体力・認知・社会的逸脱・非習慣性
    - Prompt の3種類：Spark（動機が低い人向け）/ Facilitator（能力が低い人向け）/ Signal（両方高い人向け）
- [ ]  **「Action Line」の概念を図解する**
    - Motivation × Ability が閾値を超えた時だけ行動が起きる曲線を描く
    - 既存UIのCTAをこの図に配置してみる
- [ ]  **既存サービスの画面を3つB=MAPで分析する**
    - 「Abilityを下げている摩擦」と「Motivationを上げている要素」を列挙
    - 改善案を1つ提案する
- [ ]  **Hook Model（Issue #1）との違いを整理する**
    - Fogg BM は「1回の行動を起こす」モデル
    - Hook Model は「繰り返し行動を定着させる」モデル
    - 両者の使い分けをまとめる

## 参考リソース

- [Stanford Behavior Design Lab](https://behaviordesign.stanford.edu/) — BJ Fogg 公式（無料）
- Tiny Habits: The Small Steps That Change Everything — Fogg の実践書
- original_output.md「BJ Fogg's Behavior Model」

**目安合計：3〜4時間**

## Definition of Done

- [ ]  学習内容を自分の言葉で要約している
- [ ]  画面または図で具体化している
- [ ]  ビジネス目的との接続を書いている
- [ ]  次の改善仮説が1つ以上ある
- [ ]  必要に応じてコード、Figma、参考リンクを添付している