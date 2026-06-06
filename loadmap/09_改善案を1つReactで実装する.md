## 概要

Issue #5〜#7 の改善案からコンポーネントを1つ選び、React で実装する。Issue #8 で設計したデザイントークンを使い、「デザイン意図 → コード」の一貫性を確認する。

---

## 学習順序

### ステップ1：実装するコンポーネントを選定して要件を明確にする（30分）

以下の候補から1つ選ぶ。**最初は小さいものを選ぶ**のが鉄則：

| 候補 | 難易度 | Issue |
| --- | --- | --- |
| CTAボタン（hover/focus/disabled 状態付き） | ★☆☆ | #4 |
| バリデーション付き入力フィールド | ★★☆ | #5 |
| LP ヒーローセクション | ★★★ | #7 |

選定後、以下を決めて書いておく：

- 「どの行動心理原則をこのコンポーネントで表現するか」（例：CTAボタン → 損失回避フレーミング）
- Props の一覧と型定義（実装前に設計する）

### ステップ2：プロジェクトをセットアップする（30分）

```
# Vite + React + TypeScript で新規プロジェクト作成
npm create vite@latest my-component -- --template react-ts
cd my-component && npm install

# Storybook の追加
npx storybook@latest init
```

Issue #8 で作ったトークンファイルを `src/tokens/` に置く。

### ステップ3：Figmaのデザインを見ながら実装する（2〜3時間）

Issue #7 または #5 の Figma 改善案を画面に表示しながらコーディングする。

実装の優先順位：

1. デフォルト状態を先に完成させる
2. インタラクション状態（hover / focus / active）を追加する
3. エラー状態・disabled 状態を追加する
4. レスポンシブ対応する

デザイントークンを使う箇所は必ず変数経由にする（マジックナンバーを書かない）。

### ステップ4：Storybook でストーリーを書く（1時間）

各インタラクション状態を1ストーリーずつ作る。

ストーリーのドキュメントに「この状態で何の心理原則が効いているか」をコメントで書く。

### ステップ5：アクセシビリティチェックをする（30分）

[Storybook](https://storybook.js.org/) の [a11y アドオン](https://storybook.js.org/docs/writing-tests/accessibility) を使う、または Chrome の [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) でチェックする。

違反があれば修正してからコミットする（aria-label / role / キーボード操作を確認）。

---

## やること

- [ ]  **実装するコンポーネントを選定する**（行動心理原則を明記）
- [ ]  **プロジェクトをセットアップする**（Vite + React + TypeScript + Storybook）
- [ ]  **Figmaのデザインから実装する**（デザイントークン使用・全状態を網羅）
- [ ]  **Storybookでストーリーを書く**（心理原則のコメント付き）
- [ ]  **axe-core または Lighthouse でアクセシビリティチェックを実施する**

## 参考リソース

- [Storybook 公式](https://storybook.js.org/) — コンポーネント開発環境
- [axe-core](https://github.com/dequelabs/axe-core) — アクセシビリティ自動検査
- original_output.md「コンポーネントライブラリ構築」

**目安合計：5〜6時間**

## Definition of Done

- [ ]  学習内容を自分の言葉で要約している
- [ ]  画面または図で具体化している
- [ ]  ビジネス目的との接続を書いている
- [ ]  次の改善仮説が1つ以上ある
- [ ]  必要に応じてコード、Figma、参考リンクを添付している