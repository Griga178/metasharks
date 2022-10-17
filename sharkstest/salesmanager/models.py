from django.db import models
from django.utils import timezone

# Create your models here.
class Color(models.Model):
    """
    Возможные цвета автомобилей
    """
    name = models.CharField(max_length = 200, help_text = "Введите цвет автомобиля", unique = True)

    def __str__(self):
        return self.name

class CarBrand(models.Model):
    """
    Возможные марки автомобилей
    """
    name = models.CharField(max_length = 200, help_text = "Введите марку автомобиля", unique = True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    """
    Возможные модели автомобилей
    """
    name = models.CharField(max_length = 200, help_text = "Введите модель автомобиля")
    brand_name = models.ForeignKey('CarBrand', null = False, on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.brand_name.name} {self.name}'

    class Meta:
        ordering = ["brand_name"]

class Order(models.Model):
    """
    Возможные цвета автомобилей
    """
    id = models.BigAutoField(primary_key = True)
    color_name = models.ForeignKey('Color', null = False, on_delete = models.PROTECT)
    model_name = models.ForeignKey('CarModel', null = False, on_delete = models.PROTECT)
    amount = models.IntegerField(help_text = "Введите колличество автомобилей")
    order_date = models.DateField(default = timezone.localdate, null = False)

    def __str__(self):
        return f'{self.id}. {self.model_name.brand_name.name} {self.model_name.name} - {self.color_name.name}'
    class Meta:
        ordering = ["order_date"]
