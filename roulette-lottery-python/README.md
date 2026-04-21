# ルーレット抽選システムを実装せよ Python編

ルーレット抽選で、ユーザーの予想番号のうち当選した件数を数える Python 実装です。

## 問題の整理

- `choose_number` はユーザーが選んだ予想番号の一覧
- `winning_number` は抽選で出た当選番号の一覧
- 予想番号、当選番号のどちらにも重複がありうる
- ある予想番号が当選番号に 1 回でも含まれていれば、その予想番号は当選とみなす
- 同じ予想番号が `choose_number` 側に複数ある場合は、その個数分だけ当選件数に含める
- `winning_number` 側の重複で当選件数を余分に増やしてはいけない

## ファイル構成

- `app.py`: 当選件数を数えるロジック
- `main.py`: CSV を読み込んで結果を表示する CLI
- `tests/test_app.py`: 単体テストと簡単な CLI テスト

## 実行方法

入力 CSV は 2 行構成です。

- 1 行目: `choose_number`
- 2 行目: `winning_number`

例:

```csv
1,2,3
1,3,5
```

実行:

```bash
python3 main.py sample.csv
```

出力:

```text
2
```

## テスト

```bash
python3 -m unittest discover -s tests -v
```
