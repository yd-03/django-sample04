from django.core import validators
from django.db import models


class Item(models.Model):
    SEX_CHOICES = (
        (1, "男性"),
        (2, "女性"),
    )

    name = models.CharField(
        verbose_name="名前",  # 管理画面で表示される項目名
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name="年齢",
        validators=[validators.MinValueValidator(1)],  # 1以上の値のみ許可
        blank=True,  # 空白を許可
        null=True,  # NULLを許可
    )
    sex = models.IntegerField(
        verbose_name="性別",
        choices=SEX_CHOICES,
        default=1,
    )
    memo = models.TextField(
        verbose_name="備考",
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="登録日",
        auto_now_add=True,  # 作成時に現在日時を設定
    )

    # モデルの文字列表現を返す
    def __str__(self):
        return self.name

    # モデルのメタ情報を設定
    class Meta:
        verbose_name = "アイテム"
        verbose_name_plural = "アイテム"
