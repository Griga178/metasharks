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

from rest_framework import status

class ColorSerializerVerT(APIView):
    def get(self, request, *args, **kwargs):
        colors = models.Color.objects.all()
        serializer = ColorSerializer(colors, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = ColorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CarBrandListAPIView(ListAPIView):
    serializer_class = CarBrandSerializer

    def get_queryset(self):
        return models.CarBrand.objects.all()

class CarModelListAPIView(ListAPIView):
    serializer_class = CarModelSerializer

    def get_queryset(self):
        return models.CarModel.objects.all()
