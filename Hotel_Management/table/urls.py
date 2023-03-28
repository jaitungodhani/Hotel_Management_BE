from django.urls import path, include
from .views import TableManageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("managetable", TableManageView)

urlpatterns = [
    path("table/", include(router.urls))
]
