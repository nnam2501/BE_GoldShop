from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    TypeJewerly,
    Supplier,
    Jewerly,
    Category
)

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'supplierName',
        'phoneNumber',
        'address',
        'email'
    ]
    search_fields = [
        'id',
        'supplierName',
        'address',
    ]

class JewerlyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'jewerlyName',
        'description',
        'quantity',
        'price',
        'jewerlyImage',
        # 'typeJewerly',
        'supplier',
        'active'
    ]
    search_fields = [
        'jewerlyName',
        # 'typeJewerly__typeName',
        'supplier__supplierName',
    ]
    readonly_fields = ['img']

    def img(self,Jewerly):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px' />".format(img_url=Jewerly.jewerlyImage, alt=Jewerly.jewerlyName))


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'categoryName',
        'active'
    ]
admin.site.register(TypeJewerly)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Jewerly, JewerlyAdmin)
admin.site.register(Category, CategoryAdmin)