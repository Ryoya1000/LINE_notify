## line notify

・Web スクレイピングした情報等を LINE へ通知する

## 環境構築

```
# 仮想環境に入る
pipenv shell

# スクリプト実行
python スクリプト名.py
```

## 環境変数の設定

```
# 必要な環境変数を設定する
vi ~/.zshrc

# .zshrcの中身
export LINE_NOTIFY_BLOG="LINEトークンを設定"
export USERNAME_BLOG="hogehoge"　←アクトレ
export USERNAME_BLOG_2="hogehoge"　←a8
export PASSWORD_BLOG="hogehoge"
```

## デプロイ

```
# herokuへログイン
heroku login

# herokuへデプロイする
git push heroku master

# herokuに環境変数を設定する
# 環境変数の確認
heroku config

# 環境変数の設定
heroku config:set LINE_NOTIFY_BLOG="hogehoge"

# heroku上で実行
heroku run python スクリプト名.py

```
