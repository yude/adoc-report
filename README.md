# pandoc-report
📓 アタシのレポート執筆環境

## 導入
1. 以下のソフトウェアをあなたのコンピュータにインストールしてください。\
これらのソフトウェアは、すべて Homebrew などのパッケージマネージャを用いてインストールすることができます。
   * [TeX Live](https://texwiki.texjp.org/?TeX%20Live#w628bee6)
   * [pandoc](https://pandoc-doc-ja.readthedocs.io/ja/latest/users-guide.html)
   * [Asciidoctor](https://asciidoctor.org/)
2. このリポジトリに存在するシェルスクリプト、`bdoc` をあなたのコンピュータにコピーしてください。\
`/usr/local/bin` 以下 等に配置すると、追加の設定なしで認識されます。
  * 実行権限を付与しなければならない場合があります。その場合は、以下のコマンドを実行してください。
    ```shell
    $ sudo chmod +x <bdoc へのパス>
    ```

## 使用方法
* Asciidoc 文章が存在するディレクトリで、以下のコマンドを実行してください。
  ```shell
  $ bdoc ファイル名
  # 例: bdoc report.adoc
  ```

## ライセンス
MIT License
