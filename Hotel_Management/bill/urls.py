from django.urls import path, include
from .views import BillManageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("managebill", BillManageView)

urlpatterns = [
    path("bill/", include(router.urls))
]
