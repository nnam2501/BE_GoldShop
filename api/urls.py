
from django.contrib import admin
from django.urls import path, include, re_path


from . import views

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'supplier', views.SupplierViewSet)
router.register(r'category',views.CategoryViewSet)
router.register(r'type_jewerly',views.TypeJewerlyViewSet)
router.register(r'jewerly',views.JewerlyViewSet)
router.register(r'users',views.UserViewSet, 'user')
router.register(r'customer',views.CustomerViewSet, 'customer')
router.register(r'employee',views.EmployeeViewSet, 'employee')
router.register(r'order',views.OrderViewSet)
router.register(r'order_detail',views.OrderDetailViewSet)
router.register(r'invoice',views.InvoiceViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('oauth2-info/',views.AuthInfo.as_view())
]

urlpatterns += router.urls
