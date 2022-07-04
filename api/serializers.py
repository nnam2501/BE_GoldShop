from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id','username','password','is_staff']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }

class CustomerSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id','categoryName']
        fields = '__all__'

class TypeJewerlySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = TypeJewerly
        # fields = ['id','typeName','category']
        fields = '__all__'

class JewerlySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    typeJewerly = TypeJewerlySerializer(many=True)
    supplier = SupplierSerializer()
    # jewerlyImage = Base64ImageField(max_length=None,)
    class Meta:
        model = Jewerly
        # fields = ["jewerlyName", "description","quantity" ,"price","jewerlyImage" ,"typeJewerly" ,"supplier" ,"active" ]
        fields = '__all__'

class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class InvoiceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # order = OrderSerializer()
    # employee = EmployeeSerializer()
    class Meta:
        model = Invoice
        fields = '__all__'
