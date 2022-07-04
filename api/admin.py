from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    TypeJewerly,
    Supplier,
    Jewerly,
    Category,
    User,
    Employee,
    Customer,
    Order,
    OrderDetail,
    Invoice
)


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'password',
        'email',
        'is_active'
    ]
    readonly_fields = ['id','username']
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fullName',
        'dateOfBirth',
        'gender',
        'address',
        'phoneNumber',
        'idNumber',
        'account',
        'salary',
        'active',
    ]
    search_fields = [
        'fullName',
        'gender',
        'active',
    ]

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fullName',
        'dateOfBirth',
        'gender',
        'address',
        'phoneNumber',
        'idNumber',
        'account',
        'active',
    ]
    search_fields = [
        'fullName',
        'gender',
        'active',
    ]

class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'supplierName',
        'phoneNumber',
        'address',
        'email',
        'active',
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
        'typeJewerly__typeName',
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

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'orderDate',
        'active',
    ]
    search_fields = [
        'customer'
    ]
    readonly_fields = ['id','customer','orderDate']

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'jewerly',
        'unitPrice',
        'quantity',
        'amount',
    ]

class TypeJewerlyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'typeName',
        'category',
        'active'
    ]

class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'invoiceDate',
        'order',
        'employee',
        'total',
        'active',
    ]

admin.site.register(TypeJewerly ,TypeJewerlyAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Jewerly, JewerlyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Invoice, InvoiceAdmin)