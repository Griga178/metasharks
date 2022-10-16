from django.urls import path
from . import views


urlpatterns = [
    path('color/', views.ColorListCreate.as_view(), name = 'color create list'),
    path('color/<str:pk>', views.ColorCRUD.as_view(), name = 'color crud'),
    path('brand/', views.BrandListCreate.as_view(), name = 'brands create list'),
    path('brand/<str:pk>', views.BrandCRUD.as_view(), name = 'brand crud'),
    path('model/', views.ModelListCreate.as_view(), name = 'model create list'),
    path('model/<str:pk>/', views.ModelCRUD.as_view(), name = 'model crud'),
    path('order/', views.OrderListCreate.as_view(), name='order create list'),
    path('order/<str:pk>', views.OrderCRUD.as_view(), name = 'order crud'),

    path('colors_order/', views.ColorsView.as_view(), name = 'colors orders'),
    path('brands_order/', views.BrandsView.as_view(), name = 'colors orders')

]
