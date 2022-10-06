from django.urls import path,include
from .views import TableView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('tabledata',TableView,basename='tabledata')

urlpatterns = [
   path('',include(router.urls))
]