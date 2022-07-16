# pandoc-report
📓 アタシのレポート執筆環境

## Install
* Install applications listed below.
  * TeX Live
  * pandoc
  * pygments
    ```
    pip install pygments
    ```
  * pandoc-minted
    ```
    pip install pandoc-minted
    ```
* Add `bdoc`, TeX Live, pandoc, `minted_filter.py` to your `PATH`.

## How to use
```shell
$ bdoc hoge.md
```

## License / Citations
* `bdoc`\
  MIT license.
* `minted_filter.py`\
  [Story you have created a beautiful PDF of the source code containing at Pandoc + minted](https://blog.artwolf.in/a?ID=381ab2bd-810e-42d9-a8f0-c786ec3479b2)
