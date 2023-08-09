# fastapi-deploy-sample
fastAPIのデプロイ先検証用リポジトリ

## Setup

- deta collectionsからkeyを取得し、envファイルの`DETA_PRODUCT_KEY`に貼り付け

## Usage
```
poetry run uvicorn src.main:app --host 0.0.0.0 --reload
```
