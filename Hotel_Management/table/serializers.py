from rest_framework import serializers
from .models import (
    Table
)
from order.models import Order
from django.db.models import Count, Sum, F
from item.serializers import (
    ItemSerializer
)

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class TablewithorderstatusSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Table
        fields = "__all__"

    def get_orders(slef, obj):
        orders = Order.objects.filter(table__id = obj.id).values("status").annotate(count = Count("status"))
        return orders


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
    
    

class TablewithoBilldataSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = "__all__"

    def get_total_amount(self, obj):
        total_amount = Order.objects.filter(table__id = obj.id).aggregate(amount = Sum(F("item__price")*F("quantity")))
        return total_amount["amount"]
    
    def get_orders(self, obj):
        pass
    