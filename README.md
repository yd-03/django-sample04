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
# migrationファイルを作る
python manage.py makemigrations
# migrationファイルをもとにDBに反映する
python manage.py migrate
```

- manage.py と同じ階層に db.sqlite3 というデータベースのファイルが作られ、モデルに応じたテーブルも自動で作成される
- SQL を一切書かずにデータベースを用意出来てしまう
- 本番用に MySQL や Postgres に差し替える時も settings だけを変えるだけで対応可能

## 管理サイトの設定

```bash
# 管理者用のIDとPassを設定
python manage.py createsuperuser
# 開発サーバーを起動
python manage.py runserver
```

管理者ログイン画面
http://localhost:8000/admin/

## ビューの作成

| 役割         | クラス名   | 要求する URL | HTTP メソッド |
| ------------ | ---------- | ------------ | ------------- |
| 検索一覧画面 | FilterView | /page/       | GET           |
| 詳細画面     | DetailView | /page/id     | GET           |
| 登録画面     | CreateView | /page/       | GET, POST     |
| 更新画面     | UpdateView | /page/id     | GET, POST     |
| 削除画面     | DeleteView | /page/id     | GET, POST     |

- LoginRequiredMixin: ログインが必要なビューに使用する
- reverse_lazy: URL の逆引きを遅延評価するために使用する
- DetailView, CreateView, DeleteView, UpdateView: Django の汎用ビュークラス
- FilterView: フィルタリング機能を提供するビュークラス（追加パッケージの django-filter）
- ItemFilter: Item モデル用のフィルタークラス
- ItemForm: Item モデル用のフォームクラス
- Item: 操作対象のモデル

### 基本構造

Django のルーティングは、プロジェクトレベルとアプリケーションレベルで構成される

#### プロジェクトの urls.py の例

project_name/urls.py では、アプリケーションごとの URL パターンをルーティングする

```python
# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('app/', include('app_name.urls')), # アプリのルーティング
]
```

#### アプリケーションの urls.py の例

各アプリケーションには、それぞれ urls.py を作成し、アプリケーション内のルーティングを定義する

```python
# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'), # アプリケーションのルート
path('detail/<int:id>/', views.detail, name='detail'), # 動的 URL パラメータ
]
```

#### path()関数の使い方

```python
path(route, view, kwargs=None, name=None)
```

- route: マッチする URL パターンを定義。動的セグメントには<int:id>のように記述する
- view: マッチした URL に対応するビュー関数やクラス
- kwargs: オプションの引数で、ビューに追加データを渡す
- name: URL パターンに名前を付けて、テンプレートやビュー内で参照する

#### クラスベースビューのルーティング

Django では、関数ベースビューだけでなく、クラスベースビューも使用可能。クラスベースビューを使う場合は、as_view()メソッドを指定する

```python
# app_name/urls.py
from django.urls import path
from .views import MyView

urlpatterns = [
path('my-view/', MyView.as_view(), name='my_view'),
]
```
