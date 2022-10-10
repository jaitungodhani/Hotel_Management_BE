from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import TableSerializer,CategorySerializer,ItemSerializer,OrderSerializer
from .models import Table,Category,Item,Order
import utils_files.response_handler as rh
from rest_framework.response import Response
# Create your views here.

class TableView(ViewSet):
    def list(self,request,format=None):
        all_table_obj=Table.objects.all()
        serilaize_data=TableSerializer(all_table_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

class CategoryView(ViewSet):
    def list(self,request,format=None):
        all_category_obj=Category.objects.all()
        serilaize_data=CategorySerializer(all_category_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

class ItemView(ViewSet):
    def list(self,request,format=None):
        all_item_obj=Item.objects.all()
        serilaize_data=ItemSerializer(all_item_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

class OrderView(ViewSet):
    def list(self,request,format=None):
        all_order_obj=Order.objects.all()
        serilaize_data=OrderSerializer(all_order_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

    # def create(self,request,forma)