from dataclasses import fields
from pyexpat import model
from .models import *
from rest_framework import serializers
from django.db.models import Count


class TableSerializer(serializers.ModelSerializer):
    order_status=serializers.SerializerMethodField()
    class Meta:
        model=Table
        fields="__all__"
        extra_fields=["order_status"]
    
    def get_order_status(self,table):
        order_status=Order.objects.filter(table__id=table.id).values("status").annotate(value=Count('status'))
        return order_status

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ItemSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Item
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    Item=ItemSerializer(read_only=True)
    table=TableSerializer(read_only=True)
    class Meta:
        model=Order
        fields="__all__"

class BillSerializer(serializers.ModelSerializer):
    table=TableSerializer()
    class Meta:
        model=Bill
        fields="__all__"