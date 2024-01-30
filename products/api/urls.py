from django.urls import path
from products.api.api_views.general_views import *
from products.api.api_views.product_views import *

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    # path('product/list', ProductlistAPIView.as_view(), name='product_list'),
    # path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    # path('product/detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    # path('product/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete'),
    # path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
]
 