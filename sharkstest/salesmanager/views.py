# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer, ColorSerializer, CarBrandSerializer, CarModelSerializer

from rest_framework.generics import ListAPIView
from . import models

# Create your views here.
class GetOrderInfoView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы Order
        queryset = Order.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = OrderSerializer(
            instance = queryset, # Передаём набор записей
            many = True # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)




class ColorListAPIView(ListAPIView):
    serializer_class = ColorSerializer

    def get_queryset(self):
        return models.Color.objects.all()
#
class CarBrandListAPIView(ListAPIView):
    serializer_class = CarBrandSerializer

    def get_queryset(self):
        return models.CarBrand.objects.all()

class CarModelListAPIView(ListAPIView):
    serializer_class = CarModelSerializer

    def get_queryset(self):
        return models.CarModel.objects.all()
