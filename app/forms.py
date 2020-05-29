from django import forms

from .models import Item, ItemMaster


class ItemForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """

    class Meta:
        model = Item
        fields = '__all__'

        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False


class ItemMasterForm(forms.Form):

    item_id = forms.IntegerField(
        label='商品ID',
        required=True,
        widget=forms.TextInput()
    )

    item_name = forms.CharField(
        label='商品名',
        max_length=100,
        required=True,
        widget=forms.TextInput()
    )

    item_number = forms.CharField(
        label='品番',
        max_length=100,
        required=True,
        widget=forms.TextInput()
    )

    item_price = forms.IntegerField(
        label='商品価格(税抜)',
        required=True,
        widget=forms.TextInput()
    )

    item_detail = forms.CharField(
        label='商品詳細',
        required=True,
        widget=forms.TextInput()
    )

    item_code = forms.IntegerField(
        label='janコード',
        required=True,
        widget=forms.TextInput()
    )