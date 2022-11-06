from django.urls import path,include
from .views import AllBillView, ItemView, OrderFilterView, OrderView, TableView,CategoryView,CompletedBillView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('tabledata',TableView,basename='tabledata')
router.register('categorydata',CategoryView,basename='categorydata')
router.register('itemdata',ItemView,basename='itemdata')
router.register('orderdata',OrderView,basename='orderdata')
router.register('orderdata/<str:pk>/',OrderView,basename='orderdata')
router.register('orderfilter',OrderFilterView,basename='orderfilterdata')
router.register('allbill',AllBillView,basename='allbill')
router.register('completebills',CompletedBillView,basename='completebill')

urlpatterns = [
   path('',include(router.urls))
]