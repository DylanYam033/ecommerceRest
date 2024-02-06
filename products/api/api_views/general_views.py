from rest_framework import generics
from base.api import GeneralListApiView
from products.api.serializers.general_serializers import *

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
  
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer
    
class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
