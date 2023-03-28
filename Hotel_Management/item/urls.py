from django.urls import path, include
from .views import ItemManageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("manageitem", ItemManageView)

urlpatterns = [
    path("item/", include(router.urls))
]
