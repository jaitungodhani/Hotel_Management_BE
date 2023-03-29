from rest_framework import serializers
from order.serializers import OrderSerializer
from table.serializers import TableSerializer
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only = True)
    orders = OrderSerializer(read_only = True, many=True)

    class Meta:
        model = Bill
        fields = '__all__'


class BillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    def to_representation(self, instance):
        return BillSerializer(instance).data
