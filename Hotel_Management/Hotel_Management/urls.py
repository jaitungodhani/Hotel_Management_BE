"""Hotel_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = 'Hotel Management Admin'
admin.site.site_title = 'Hotel Management Admin'
admin.site.index_title = 'Welcome to Hotel Management Admin Dashboard'

schema_view = get_schema_view(
   openapi.Info(
      title="Hotel Management APIs",
      default_version='v1',
      description="API for Hotel Management Application",
      terms_of_service="",
      contact=openapi.Contact(email="info@servicepack.ai"),
      license=openapi.License(name="Commercial"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_login/', include("auth_login.urls")),
    path('api/',include("all_api.urls")),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
