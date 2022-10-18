from .models import Color, CarBrand, CarModel, Order
from .serializers import ColorSerializer,  CarBrandSerializer, CarModelSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView

from django.db.models import Count, F, Sum
from rest_framework.views import APIView
from rest_framework.response import Response

from.tables import OrderTable, OrderFilter
from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

#                - - - - * - - - - ЦВЕТА АВТО - - - - * - - - -
class ColorListCreate(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ColorCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

#                 - - - - * - - - - МОДЕЛИ АВТО - - - - * - - - -
class ModelListCreate(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class ModelCRUD(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

#                 - - - - * - - - - МАРКИ АВТО - - - - * - - - -
class BrandListCreate(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class BrandCRUD(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

#                 - - - - * - - - - ЗАКАЗЫ АВТО - - - - * - - - -
class OrderListCreate(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# api список цветов с указанием количества заказанных авто каждого цвета
class ColorsView(APIView):
    def get(self, req):
        qs = Order.objects.annotate(color_id = F('color_name')).values('color_id').annotate(cars_amount = Sum('amount'))
        sum_dict = {}
        for el in qs:
            color_name = Color.objects.get(pk = el['color_id']).name
            cars_amount = el['cars_amount']
            if color_name in sum_dict:
                sum_dict[color_name] += cars_amount
            else:
                sum_dict[color_name] = cars_amount
        return Response(f'{sum_dict}')

# api список марок с указанием количества заказанных авто
class BrandsView(APIView):
    def get(self, req):
        qs = Order.objects.annotate(model = F('model_name')).values('model').annotate(cars_amount = Sum('amount'))
        sum_dict = {}
        for el in qs:
            model_obj = CarModel.objects.get(pk = el['model'])
            model_name = f'{model_obj.brand_name} {model_obj.name}'
            cars_amount = el['cars_amount']
            if model_name in sum_dict:
                sum_dict[model_name] += cars_amount
            else:
                sum_dict[model_name] = cars_amount
        return Response(f'{sum_dict}')

# таблица списка заказов
class FilteredOrderListView(SingleTableMixin, FilterView):
    table_class = OrderTable
    model = Order
    template_name = 'order_list.html'
    paginate_by = 10
    filterset_class = OrderFilter

# SWAGGER

# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title = 'api')

# urlpatterns += [url(r'^$', schema_view)]
