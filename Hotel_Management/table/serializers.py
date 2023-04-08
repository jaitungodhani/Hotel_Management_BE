from rest_framework import serializers
from .models import (
    Table
)
from bill.models import Bill
from order.models import Order
from django.db.models import Count, Sum, F
from item.serializers import (
    ItemSerializer
)

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
    

class TablewithorderdataSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()
    status_based_order_count = serializers.SerializerMethodField()
   
    class Meta:
        model = Table
        fields = "__all__"

    def get_total_amount(self, obj):
        total_amount = Order.objects.filter(table__id = obj.id).exclude(id__in=Bill.objects.filter(table__id=obj.id).values("orders")).aggregate(amount = Sum(F("item__price")*F("quantity")))
        return str(total_amount["amount"])
    
    def get_orders(self, obj):
        orders = Order.objects.filter(table__id = obj.id).exclude(id__in=Bill.objects.filter(table__id=obj.id).values("orders")).all()
        return OrderSerializer(orders, many=True).data
    
    def get_status_based_order_count(slef, obj):
        orders = Order.objects.filter(table__id = obj.id).exclude(id__in=Bill.objects.filter(table__id=obj.id).values("orders")).values("status").annotate(count = Count("status"))
        return list(orders)