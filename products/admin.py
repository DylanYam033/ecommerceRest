from django.contrib import admin
from products.models import *

# Register your models here.

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(Product)
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)