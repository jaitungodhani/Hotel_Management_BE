from rest_framework import serializers
from .models import (
    Table
)
from order.models import Order
from django.db.models import Count


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