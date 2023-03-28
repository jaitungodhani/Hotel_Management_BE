from django.urls import path, include
from .views import CategoryManageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("managecategory", CategoryManageView)

urlpatterns = [
    path("category/", include(router.urls))
]
