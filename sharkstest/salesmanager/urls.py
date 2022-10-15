from django.urls import path
from . import views


urlpatterns = [
    path('salesmanager/', views.GetOrderInfoView.as_view()),
    path('colors/', views.ColorListAPIView.as_view(), name='api_colors'),
    path('colorsVT/', views.ColorSerializerVerT.as_view(), name='api_colorsT'),
    path('brands/', views.CarBrandListAPIView.as_view(), name='api_brands'),
    path('models/', views.CarModelListAPIView.as_view(), name='api_models'),
]
