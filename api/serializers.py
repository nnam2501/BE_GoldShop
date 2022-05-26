from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','categoryName']

class TypeJewerlySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = TypeJewerly
        fields = ['id','typeName','category']

class JewerlySerializer(serializers.ModelSerializer):
    typeJewerly = TypeJewerlySerializer(many=True)
    class Meta:
        model = Jewerly
        # fields = ["jewerlyName", "description","quantity" ,"price","jewerlyImage" ,"typeJewerly" ,"supplier" ,"active" ]
        fields = '__all__'