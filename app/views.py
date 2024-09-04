from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item


# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, FilterView):
    # モデルとフィルタークラスを指定
    model = Item
    filterset_class = ItemFilter

    # デフォルトの並び順を新しい順に設定
    queryset = Item.objects.all().order_by("-created_at")

    # クエリが指定されていない場合に全件検索を行うための設定
    strict = False

    # 1ページあたりの表示件数を設定
    paginate_by = 10

    # 検索条件をセッションに保存または呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session["query"] = request.GET
        else:
            request.GET = request.GET.copy()
            if "query" in request.session.keys():
                for key in request.session["query"].keys():
                    request.GET[key] = request.session["query"][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("index")


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("index")


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy("index")
