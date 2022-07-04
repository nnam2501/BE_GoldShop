from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def get_current_user(self,request):
        return Response(self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)

class AuthInfo(APIView):
    def get(self,request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(active=True)
    serializer_class = CustomerSerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Customer.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Customer.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=CustomerSerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(active=True)
    serializer_class = EmployeeSerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Employee.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Employee.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=EmployeeSerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Supplier.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Supplier.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=SupplierSerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated]
    # @action(methods=['get'], detail=True)
    # def getAllSupplier(self, request):
    #     try:
    #         s = Supplier.objects.all()
    #     except Supplier.DoesNotExits:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #     return Response(data=SupplierSerializer(s,context={"request":request}).data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Category.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Category.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=CategorySerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class TypeJewerlyViewSet(viewsets.ModelViewSet):
    queryset = TypeJewerly.objects.filter(active=True)
    serializer_class = TypeJewerlySerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = TypeJewerly.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except TypeJewerly.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=TypeJewerlySerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class JewerlyViewSet(viewsets.ModelViewSet):
    queryset = Jewerly.objects.filter(active=True)
    serializer_class = JewerlySerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Jewerly.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Jewerly.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=JewerlySerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Order.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Order.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=OrderSerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.filter(active=True)
    serializer_class = InvoiceSerializer

    @action(methods=['post'], detail=True)
    def delete_tmp(self, request, pk):
        try:
            tmp = Invoice.objects.get(pk=pk)
            tmp.active = False
            tmp.save()
        except Invoice.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=InvoiceSerializer(tmp, context={"request": request}).data, status=status.HTTP_200_OK)
