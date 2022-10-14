from . import models
from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    color_name = serializers.CharField()#source = 'Color.name'
    model_name = serializers.CharField()#source = 'CarModel.name')
    brand_name = serializers.CharField(source = 'model_name.brand_name.name')
    ammount = serializers.IntegerField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ('__all__')
#
class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarBrand
        fields = ('__all__')
#
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields = ('__all__')
