from . import models
from rest_framework import serializers


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = ('__all__')

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarBrand
        fields = ('__all__')

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
