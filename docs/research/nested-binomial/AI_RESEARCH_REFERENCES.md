# AIによる数学研究・自動証明の参考資料

以下11件のREADME抜粋を実際にDeepSeekへ共有し、適用範囲の評価を依頼した。固定コミットと入力ハッシュは `AI_RESEARCH_REFERENCE_CATALOG.json` に記録する。モデルが永久に記憶したという意味ではなく、研究状態をAPIへ毎回読み込む。

- [deepseek-ai/DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2/blob/e598a57ea3284997d4a2a168a069fdd5064afbc8/README.md)：サブゴール分解と、モデルの説明を形式証明へ接続する設計。今回のAPIモデルとは別モデル。
- [google-deepmind/alphageometry](https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/README.md)：合成幾何での記号推論との組合せ。今回の代数幾何・数論へ直接適用したとはしない。
- [google-deepmind/formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/3f4490479b53386e1c18d2cccf4f1164c16655ca/README.md)：未解決命題の正確なLeanステートメントを先に固定し、証明の有無と分離する。
- [facebookresearch/Evariste](https://github.com/facebookresearch/Evariste/blob/ef43511f2d234bcb28e380388b8fe0d06a4d93a7/README.md)：HyperTree Proof Searchの探索方針の参考。READMEがアーカイブ用途を明記しており、稼働基盤として導入していない。
- [project-numina/kimina-lean-server](https://github.com/project-numina/kimina-lean-server/blob/fb2393de3461db35eda4c714e3fd21187e92ec90/README.md)：Lean REPLと並列検証の構成。今回はインストール・移行していない。
- [lean-dojo/LeanDojo](https://github.com/lean-dojo/LeanDojo/blob/7a9f600b250a89a62e991c05ffe81ba033018e6e/README.md)：前提・証明状態の抽出。READMEで旧版とされているため後継版も確認した。
- [lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot/blob/078135523a51e34b6a095bb2e4088ab4ee0161f0/README.md)：モデルによるタクティクス提案と前提選択の参考。モデル重みは導入していない。
- [leanprover-community/repl](https://github.com/leanprover-community/repl/blob/6a2be396449a5213a36748ca7682d16d54a1ca4a/README.md)：失敗位置の実ゴールを返す設計。今回はコマンドラインLeanの診断用状態取得を使った。
- [leanprover-community/aesop](https://github.com/leanprover-community/aesop/blob/7d11bfa88558f8d3d90afdf6bd877ed70001498d/README.md)：規則に基づく証明探索。Mathlib.Tactic経由の固定依存は利用可能だが、公開HEADへ更新していない。
- [google-deepmind/alphageometry2](https://github.com/google-deepmind/alphageometry2/blob/251e7e16f0bba8ac7c83cdea789fccc195d0c0c7/README.md)：READMEで案内された後継版も参照。対象は平面幾何であり、数論の楕円曲線とは区別する。
- [lean-dojo/LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2/blob/f3b01b180e7429ed5389c2409ed14ce9ede93987/README.md)：後継の証明環境・前提抽出の参考。現行Lean/mathlibへの互換性を確認済みとはしない。

## この研究で実装した部分

固定した定理文への証明生成、1定理ずつのLean実行、成功済み証明の固定、失敗時の別評価呼び出し、実ゴール状態の取得、不明な定理名からの固定mathlibソース検索、モデルへの診断返送、ハッシュ付きの実行記録を実装した。これらは公開手法を参考にした独自の接続であり、各システム全体や外部モデルを導入したものではない。

OpenAI lean-gym・EvalsとAnthropicのevaluator-optimizerは `v10_formal/RESEARCH_WORKFLOW.md` の固定リンクを参照。古典的な楕円曲線の座標変換自体を「最先端の新定理」とは呼ばない。
