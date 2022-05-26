from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *

# Create your views here.
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer
    # permission_classes = [permissions.IsAuthenticated]

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