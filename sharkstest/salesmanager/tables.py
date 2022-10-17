import django_tables2 as tables
# from django_tables2 import A
import django_filters
from django import forms
from .models import Order


class OrderTable(tables.Table):
    order_date = tables.Column(verbose_name = "Дата заказа")
    brand = tables.Column(accessor = "model_name.brand_name", verbose_name = "Марка")
    model = tables.Column(accessor = "model_name.name", verbose_name = "Модель")
    color_name = tables.Column(verbose_name = "Цвет")
    amount = tables.Column(verbose_name = "Количество")
    class Meta:
        model = Order
        sequence = ("order_date", "brand", "model", "color_name", "amount", "id")
        attrs = {'class': 'paleblue'}
        exclude = ('id', "model_name")




class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['model_name__brand_name']
