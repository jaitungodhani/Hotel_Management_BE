from dataclasses import fields
from pyexpat import model
from .models import *
from rest_framework.serializers import ModelSerializer

class TableSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ItemSerializer(ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Item
        fields="__all__"

class OrderSerializer(ModelSerializer):
    Item=ItemSerializer()
    class Meta:
        model=Order
        fields="__all__"

class BillSerializer(ModelSerializer):
    table=TableSerializer()
    class Meta:
        model=Bill
        fields="__all__"