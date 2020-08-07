# Get IT Word Tool

## setup

```
# コンテナの起動
$ docker-compose up -d

# コンテナに入る
$ docker exec -it getitword bash

# clientId,clientSecretを設定する
$ vi getitword/client_credentials.json
```

## how to use

```
# ワードを取得する
$ python getitword --urls "https://example.com"
$ python getitword --urls "https://example.com" "https://example.com/xxx"
```