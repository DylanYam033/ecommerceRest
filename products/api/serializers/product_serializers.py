from products.models import Product
from rest_framework import serializers
from products.api.serializers.main_serializers import *

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image != '' else '',
            'mesure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        } 