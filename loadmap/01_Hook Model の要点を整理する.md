## 概要

Nir Eyal の Hook Model（Trigger → Action → Variable Reward → Investment）を習得し、実プロダクトへの適用パターンを整理する。

***

## 学習順序

### ステップ1：理論インプット（1〜2時間）

書籍なしで始めるなら Nir & Far ブログ を先に読む（無料・英語）。

以下の順に4本読むと4ステップを網羅できる：

* [x] 1. [How to Manufacture Desire](https://www.nirandfar.com/how-to-manufacture-desire/) — 4ステップの概要

* [ ] 2. [Habits Begin with a Trigger](https://www.nirandfar.com/how-to-trigger-product-usage-that-sticks/) — 外部→内部Triggerへの転換

* [ ] 3. [Want To Hook Users? Drive Them Crazy](https://www.nirandfar.com/want-to-hook-your-users-drive-them-crazy/) — Variable Reward の Hunt/Self/Tribe

* [ ] 4. [Make Your Users Do the Work](https://www.nirandfar.com/makeyourusersdothework/) — Investment が次の Trigger を強化する仕組み

補足：[The Billion Dollar Mind Trick](https://www.nirandfar.com/billion-dollar-mind-trick-2/) は内部Triggerを深掘りしたい場合に読む。

4ステップを1枚の図（Trigger → Action → Variable Reward → Investment）に手書きでまとめる。

書籍を読むなら『Hooked』の第1〜4章（各ステップ1章ずつ）を読んで同様にまとめる。

### ステップ2：概念を自分の言葉で整理（30分）

* [ ] 1. **Trigger**：「なぜ今そのアプリを開くのか」を考える。通知（外部）vs 退屈・不安（内部）
* [ ] 2. **Action**：「最もシンプルな行動とは何か」 — Fogg BM と繋がる部分なので Issue #2 と並行でも可
* [ ] 3. **Variable Reward**：なぜ「可変」なのかがポイント。SNSのフィードをスクロールする自分を観察する
* [ ] 4. **Investment**：Twitterのフォロー・プロフィール設定が「なぜ次のTriggerを強化するか」を言語化する

### ステップ3：実プロダクトに当てはめる（1時間）

**Duolingo 1サービスに絞って深くやる**のが効果的。

| ステップ            | Duolingo での対応箇所                 |
| --------------- | ------------------------------- |
| Trigger         | 毎日リマインド通知（外部）→ 「英語力を保ちたい」不安（内部） |
| Action          | 1問だけ解く（Ability が高い）             |
| Variable Reward | 正解時のアニメーション・ストリーク・XP            |
| Investment      | XP・リーグ・連続日数の蓄積                  |

スクショを撮って4ステップの対応箇所に矢印を引く → そのままアウトプットになる。

### ステップ4：エンジニア視点でまとめる（30分）

Investment フェーズを「実装でどう強化できるか」を自分のコードで考える。

* ユーザーデータの蓄積（お気に入り・設定・履歴）→ 次回起動時の内部 Trigger になる

* Push通知のタイミング設計（内部 Trigger に転換するまでの期間をどう計算するか）

***

## やること

* [ ] **4ステップを図解する**

* Trigger（外部: 通知・広告 / 内部: 感情・習慣）の違いを説明

* Action（Fogg BMの「最もシンプルな行動」との接続を整理）

* Variable Reward の3種類：Hunt（情報・資源）/ Self（達成感）/ Tribe（社会的承認）

* Investment フェーズがなぜ次のTriggerを強化するか書く

* [ ] **実プロダクトで当てはめる（2〜3サービス）**

* Twitter/X、Duolingo、LINEなどから選定

* 各ステップが画面のどこに対応するかをスクショ付きで記録

* [ ] **エンジニア視点でまとめる**

* Investment フェーズを実装で強化する手法（データ蓄積・カスタマイズ）

* Push通知と内部Triggerの設計パターン

## 参考リソース

* 書籍『Hooked ハマるしかけ』（Nir Eyal）優先度1

* Nir & Far blog — 著者公式ブログ（無料）

* original\_output.md「フェーズ1：基礎理論の構築」

**目安合計：3〜4時間**

## Definition of Done

* [ ] &#x20;学習内容を自分の言葉で要約している

* [ ] &#x20;画面または図で具体化している

* [ ] &#x20;ビジネス目的との接続を書いている

* [ ] &#x20;次の改善仮説が1つ以上ある

* [ ] &#x20;必要に応じてコード、Figma、参考リンクを添付している
