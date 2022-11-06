from functools import partial
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import TableSerializer,CategorySerializer,ItemSerializer, \
    OrderSerializer,AllBillSerializer,BillSerializer
from .models import Table,Category,Item,Order,Bill
import utils_files.response_handler as rh
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from itertools import chain

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
        all_order_obj=Order.objects.order_by("-status","create_at").all()
        serilaize_data=OrderSerializer(all_order_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

    def retrieve(self,request,pk=None):
        all_order_obj=Order.objects.filter(table_id=pk).all()
        serialize_data=OrderSerializer(all_order_obj,many=True)
        r=rh.ResponseMsg(data=serialize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)
    
    def create(self,request):
        serializers=OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(Item_id=request.data["Item_id"],table_id=request.data["table"])
            r=rh.ResponseMsg(data=serializers.data,error=False,msg="create Successfully!!!")
            return Response(r.response)
        r=rh.ResponseMsg(data={},error=True,msg=serializers.errors)
        return Response(r.response)

    def update(self,request,pk=None):
        order_data=Order.objects.filter(pk=pk).first()
        serializers=OrderSerializer(order_data,request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            r=rh.ResponseMsg(data=serializers.data,error=False,msg="update Successfully!!!")
            return Response(r.response)
        r=rh.ResponseMsg(data={},error=True,msg=serializers.errors)
        return Response(r.response)

    def destroy(self, request, pk=None):
        obj=Order.objects.get(pk=pk)
        obj.delete()
        r=rh.ResponseMsg(data={},error=False,msg="Delete Order Succssfully!!!")
        return Response(r.response)

class OrderFilterView(ViewSet):
    def create(self,request):
        tables=request.data.get("tables")
        items=request.data.get("items")
        status=request.data.get("status")
        print(tables,items,status)
        all_order_obj=Order.objects.order_by("-status","create_at").all()
        all_order_obj=Order.objects.filter(table__name__in=tables,id__in=all_order_obj).all() if tables else all_order_obj
        all_order_obj=Order.objects.filter(Item__name__in=items,id__in=all_order_obj).all() if items else all_order_obj
        all_order_obj=Order.objects.filter(status__in=status,id__in=all_order_obj).all() if status else all_order_obj
        serilaize_data=OrderSerializer(all_order_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)

class AllBillView(ViewSet):
    def list(self,request):
        all_bill_obj=Table.objects.all()
        serialize_data=AllBillSerializer(all_bill_obj,many=True)
        r=rh.ResponseMsg(data=serialize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)
    
    def create(self,request):
        serialize=BillSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            id=serialize.data["id"]
            Order.objects.filter(table__id=request.data["table"],pay=False).update(pay=True,bill=id)
            r=rh.ResponseMsg(data={},error=False,msg="create Successfully!!!")
            return Response(r.response)
        r=rh.ResponseMsg(data={},error=True,msg=serialize.errors)
        return Response(r.response)

class CompletedBillView(ViewSet):
    def list(self,request):
        all_bill_obj=Bill.objects.filter(pay=True).all()
        serialize_data=BillSerializer(all_bill_obj,many=True)
        r=rh.ResponseMsg(data=serialize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)        
