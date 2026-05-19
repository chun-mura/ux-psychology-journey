# Behavioral Design Engineer Roadmap

マーケティング、行動心理、デザインを横断して学び、**ビジネス価値を画面で生み出し、技術で実現できるエンジニア**を目指すための学習リポジトリです。

このリポジトリでは、行動心理学を土台にしながら、UX/UIデザイン、マーケティング、実装、検証までを一貫して学びます。

## Purpose

このリポジトリの目的は次の3つです。

- 行動心理・マーケティング・デザインを別々に学ぶのではなく、ひとつの実践スキルとして統合する
- 学んだ理論を Figma、UI設計、実装、A/Bテスト、改善提案まで落とし込む
- 学習メモ置き場ではなく、将来的に再利用できる意思決定ログとポートフォリオに育てる

## Learning Themes

### 1. Behavioral Psychology

人がなぜその行動を取るのか、どのような条件で意思決定が変わるのかを理解します。

主な学習対象:

- Fogg Behavior Model
- Hook Model
- Nudge Theory
- Dual Process Theory
- Cognitive Biases
- Behavior Design Strategies（Conscious Action / Habit Formation / 注意散漫環境への対策）

### 2. Design

見た目の良さだけでなく、情報設計・視線誘導・操作しやすさ・アクセシビリティまで含めて学びます。

主な学習対象:

- Typography
- Color Theory
- Layout and Grid
- Information Architecture
- Interaction Design
- Accessibility
- Design Systems
- Design Thinking（Empathy / Define / Ideate / Prototype / Test）

### 3. Marketing

ユーザー理解から価値提案、訴求、改善までの流れを学び、画面設計とビジネス成果をつなげます。

主な学習対象:

- STP
- 4P / 7P
- Customer Journey
- Value Proposition
- Positioning
- Conversion Optimization
- Experiment Design
- Marketing Psychology（返報性 / バンドワゴン効果 / 希少性 / 損失回避 / アンカリング）
- Business Model Canvas / Lean Canvas
- 競合分析（PEST分析 / ファイブフォース分析 / 3C分析）

## Roadmap

### Phase 1: Foundations (Month 1–3)

最初のフェーズでは、人間理解とデザイン基礎を固めます。

**Goal**

- 行動心理の基本理論を説明できる
- 良いUIの共通原則を言語化できる
- マーケティングの基本フレームワークを使える

**Output**

- 読書ノート
- 既存サービスのUI分析メモ
- デザイン心理学の要約資料

### Phase 2: Applied Design (Month 4–6)

このフェーズでは、心理学とデザイン原則を画面設計に適用します。

**Goal**

- CTA、導線、入力フォーム、オンボーディングの改善意図を説明できる
- 画面上の摩擦と動機づけを分析できる
- 既存UIをビジネス目的から再設計できる

**Output**

- Figma改善案
- 画面ごとの改善レポート
- ビフォーアフター比較

### Phase 3: Build and Measure (Month 7–12)

最後のフェーズでは、設計した内容をコードに落とし、結果を計測して改善します。

**Goal**

- デザイン意図をコードに落とせる
- 仮説、実装、検証のループを回せる
- 改善結果を定量・定性の両面で評価できる

**Output**

- 実装済みUIコンポーネント
- Storybook or UI snapshots
- A/Bテスト仮説メモ
- 振り返りレポート

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── notes/
│   ├── summaries/
│   ├── reviews/
│   └── reports/
├── research/
│   ├── psychology/
│   ├── marketing/
│   └── design/
├── figma/
│   ├── wireframes/
│   └── redesigns/
├── experiments/
│   ├── landing-pages/
│   ├── onboarding/
│   └── forms/
├── components/
│   ├── ui/
│   └── patterns/
└── tasks/
    ├── monthly/
    └── backlog/
```

構造は「資料」「試作」「実装」「振り返り」を分ける形にしています。学習記録だけで終わらせず、実践物と意思決定ログを残すことで、後からポートフォリオや提案資料へ転用しやすくなります。

## GitHub Workflow

GitHub Projects を活用し、作業項目を整理し、優先順位と進捗を見える化します。

### Recommended labels

- `area:psychology`
- `area:marketing`
- `area:design`
- `area:implementation`
- `type:note`
- `type:experiment`
- `type:review`
- `priority:high`
- `priority:medium`
- `priority:low`

### Recommended issue types

- Learning note
- Book summary
- UI critique
- Redesign task
- Implementation task
- Experiment plan
- Retrospective

### Recommended milestones

- Month 01: Foundations
- Month 02: Decision Making
- Month 03: Visual Design
- Month 04: UX Patterns
- Month 05: Marketing Basics
- Month 06: Conversion Design
- Month 07: Redesign Project 1
- Month 08: Redesign Project 2
- Month 09: Implementation Project
- Month 10: Measurement and Testing
- Month 11: Portfolio Refinement
- Month 12: Final Review

## Engineer-Specific Strategy

エンジニアとしての技術スキルを行動デザインに直結させる領域。

### コードとデザインの橋渡し

- **Design Tokens 管理**: TypeScript でのトークン定義と Figma Variables の同期
- **コンポーネントライブラリ構築**: Storybook と Figma Code Connect の統合
- **A/Bテストフレームワーク**: Next.js での実装とデータ分析
- **アクセシビリティ自動化**: axe-core / Lighthouse の CI/CD 統合

### AI 時代の優位性

- 行動心理原則を明示した AIプロンプトでデザイン意図を正確に伝える
- デザイントークン → コンポーネント → テストの自動生成ワークフロー構築
- 定量データから行動仮説を立て、AI で実装案を生成するデータドリブンな改善サイクル

## Study Loop

学習効率を高めるには、インプットとアウトプットを分けず、成果物を作りながら定着させる進め方が有効です。

1. **学ぶ**: 書籍、論文、記事、動画から理論を理解する
2. **分析する**: 既存サービスのUIや導線を分解する
3. **作る**: Figmaで改善案を作る
4. **実装する**: コードに落とす
5. **振り返る**: なぜその設計にしたかを記録する
6. **測る**: KPIやユーザー反応で妥当性を確認する

### 週次サイクル

| 活動 | 目安時間 |
|------|---------|
| 理論学習（書籍・オンラインコース） | 週5時間 |
| 実践演習（既存UIの分析と改善提案） | 週3時間 |
| コーディング（デザインシステムの実装） | 週2時間 |
| 振り返り（学んだことのドキュメント化） | 週1時間 |

## Definition of Done

各Issueは、次の条件を満たしたら完了とします。

- 学習内容を自分の言葉で要約している
- 画面または図で具体化している
- ビジネス目的との接続を書いている
- 次の改善仮説が1つ以上ある
- 必要に応じてコード、Figma、参考リンクを添付している

## Initial Backlog

最初の10件として、次のIssue作成を想定しています。

1. Hook Model の要点を整理する
2. Fogg Behavior Model をUI改善に当てはめる
3. STPとペルソナ設計を整理する
4. 良いCTAの事例を10件収集する
5. フォームUXの悪い例と改善案をまとめる
6. SaaSオンボーディングを3サービス比較する
7. LPのファーストビュー改善案を作る
8. デザイントークン設計の方針を作る
9. 改善案を1つReactで実装する
10. 実装結果を振り返りレポートにまとめる

## Operating Policy

- 毎週最低1つは Issue を完了させる
- 毎月1本は「分析 → 改善案 → 実装 or 検証」まで通す
- 学習メモよりも、判断理由と再利用可能なパターンの蓄積を優先する
- デザインの感覚だけでなく、行動心理とマーケティング仮説で説明する
- 実装可能性まで含めて考える

## Long-term Goal

最終的な目標は、見た目を整えるだけの人ではなく、ユーザー行動と事業成果を理解し、画面で価値を設計し、それを実装・改善までつなげられる人材になることです。

## Community

- **Behavior Design Lab**（Stanford）― BJ Fogg 公式リソース・コミュニティ
- **UX StackExchange** ― 実務者によるQ&A
- **Product Design Weekly** ― デザイン事例の週次配信

## Recommended Books

優先度順に並べています。

1. **『Hooked ハマるしかけ』**（Nir Eyal）― 習慣化デザインの教科書
2. **『予想どおりに不合理』**（ダン・アリエリー）― 行動経済学の入門
3. **『USJを劇的に変えた、たった1つの考え方』**（森岡毅）― 実践的マーケティング戦略
4. **『誰のためのデザイン？』**（ドン・ノーマン）― UXデザインの古典
5. **『実戦マーケティング戦略』**（佐藤義典）― 理論を実践に落とし込む

## References

このロードマップは以下のリソースを参考にしています：

1. UX Design Roadmap - roadmap.sh: https://roadmap.sh/ux-design
2. Projects のベスト プラクティス - GitHub Docs: https://docs.github.com/ja/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects
3. マーケター1年目の自分に贈る学習ロードマップ: https://note.com/gtminami/n/n47df17ece4f2
4. Combining UX design and psychology to change user behaviour: https://uxdesign.cc/combining-ux-design-and-psychology-to-change-user-behaviour-39d27730434a
5. UX Design Learning Roadmap - Coursera: https://www.coursera.org/resources/ux-learning-roadmap
6. The Intersection of Psychology and UX: Exploring Behavioral Design: https://blog.uxtweak.com/behavioral-design/
7. Nielsen Norman Group（UX研究の権威による記事・ガイド）: https://www.nngroup.com/
8. Laws of UX（心理原則をデザインに応用）: https://lawsofux.com/
9. Behavioral Design Academy（無料ビデオシリーズ）: https://www.behavioraldesign.academy/
10. Marketing Psychology & Neuromarketing - Coursera: https://www.coursera.org/specializations/marketing-psychology

---

**作成者**: nakamura kohki
**開始日**: 2026年5月
