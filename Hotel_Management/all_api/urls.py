from django.urls import path,include
from .views import ItemView, OrderView, TableView,CategoryView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('tabledata',TableView,basename='tabledata')
router.register('categorydata',CategoryView,basename='categorydata')
router.register('itemdata',ItemView,basename='itemdata')
router.register('orderdata',OrderView,basename='orderdata')
router.register('orderdata/<str:pk>/',OrderView,basename='orderdata')

urlpatterns = [
   path('',include(router.urls))
]