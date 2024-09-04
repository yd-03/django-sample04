from django_filters import FilterSet, filters

from .models import Item


# カスタムの並び替えフィルタークラス
class MyOrderingFilter(filters.OrderingFilter):
    # 降順のフォーマットを指定
    descending_fmt = "%s （降順）"


# Itemモデル用のフィルターセットクラス
class ItemFilter(FilterSet):
    # 名前フィールドの部分一致フィルター
    name = filters.CharFilter(label="名前", lookup_expr="contains")
    # 備考フィールドの部分一致フィルター
    age = filters.CharFilter(label="備考", lookup_expr="contains")

    # 並び替えフィルター
    order_by = MyOrderingFilter(
        fields=(
            ("name", "name"),  # 名前で並び替え
            ("age", "age"),  # 年齢で並び替え
        ),
        field_labels={
            "name": "名前",
            "age": "年齢",
        },
        label="並び順",
    )

    class Meta:
        model = Item
        fields = ("name", "sex", "memo")  # フィルター対象のフィールド
