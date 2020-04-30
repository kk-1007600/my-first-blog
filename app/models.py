from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 商品ID
    item_id = models.IntegerField(
        verbose_name='商品ID',
        blank=True,
        null=True,
    )

    # 商品名
    item_name = models.CharField(
        verbose_name='商品名',
        max_length=100,
        blank=True,
        null=True,
    )

    # 品番
    item_number = models.CharField(
        verbose_name='品番',
        max_length=100,
        blank=True,
        null=True,
    )

    # 商品価格(税別)
    item_price = models.IntegerField(
        verbose_name='商品価格(税抜)',
        blank=True,
        null=True,
    )

    # 商品区分
    item_category = models.CharField(
        verbose_name='商品区分',
        max_length=100,
        blank=True,
        null=True,
    )

    # 商品種類
    item_kind = models.CharField(
        verbose_name='商品種類',
        max_length=100,
        blank=True,
        null=True,
    )

    # 商品詳細
    item_detail = models.TextField(
        verbose_name='商品詳細',
        blank=True,
        null=True,
    )

    # 商品メモ
    item_memo = models.TextField(
        verbose_name='商品詳細',
        blank=True,
        null=True,
    )

    # janコード
    item_code = models.IntegerField(
        verbose_name='janコード',
        blank=True,
        null=True,
    )

    # 在庫数
    item_stock = models.IntegerField(
        verbose_name='在庫数',
        blank=True,
        null=True,
    )

    # 単品重量(g)
    item_weight = models.IntegerField(
        verbose_name='単品重量(g)',
        blank=True,
        null=True,
    )

    # 登録日
    item_resist_date = models.DateField(
        verbose_name='登録日',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
