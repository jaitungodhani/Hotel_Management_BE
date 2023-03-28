from django.urls import path, include
from .views import OrderManageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("manageorder", OrderManageView)

urlpatterns = [
    path("order/", include(router.urls))
]
