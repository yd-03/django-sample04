# django-sample04

## 追加パッケージ

| パッケージ名        | 説明                                          |
| ------------------- | --------------------------------------------- |
| django-crispy-forms | 入力フォームの HTML を Bootstrap に対応させる |
| django-filter       | 検索機能を追加する                            |

## モデルフィールド一覧

| オプション   | 説明                                     |
| ------------ | ---------------------------------------- |
| auto_now_add | 追加時に現在時間を設定                   |
| blank        | 必須入力（デフォルトは True なので注意） |
| choices      | 選択支の自動生成                         |
| default      | デフォルト値                             |
| max_length   | 文字長                                   |
| validators   | バリデーションの追加                     |
| verbose_name | フォーム自動生成で見出しとして使う       |

[詳細はこちら](https://docs.djangoproject.com/ja/2.1/ref/models/fields/#field-types)

## DB 作成

```bash
python manage.py makemigrations
python manage.py migrate
```

## 管理サイトの設定

```bash
# 管理者用のIDとPassを設定
python manage.py createsuperuser
# 開発サーバーを起動
python manage.py runserver
```

管理者ログイン画面
http://localhost:8000/admin/
