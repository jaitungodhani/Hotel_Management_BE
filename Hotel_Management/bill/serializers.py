from rest_framework import serializers
from order.serializers import OrderSerializer
from table.serializers import TableSerializer
from .models import Bill
from order.models import Order


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

    def validate(self, attrs):
        orders = attrs["orders"]
        for order in orders:
            if Order.objects.filter(status__in = ["Waiting", "Prepairing", "Cooked"], id=str(order)).exists():
                raise serializers.ValidationError(f"All orders not Delivered, first Delivered this {str(order)}!!!")
        return attrs
        

    def to_representation(self, instance):
        return BillSerializer(instance).data
