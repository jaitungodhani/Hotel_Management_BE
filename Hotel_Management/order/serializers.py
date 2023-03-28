from .models import Order
from rest_framework import serializers
from table.serializers import TableSerializer
from item.serializers import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only = True)
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        return OrderSerializer(instance).data