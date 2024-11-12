# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import BookViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# تنظیم Router برای ViewSets
router = DefaultRouter()
router.register(r'books', BookViewSet)

# تنظیم Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Simple API",
      default_version='v1',
      description="A simple API to manage books",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include(router.urls)),

]