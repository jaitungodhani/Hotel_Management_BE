from .models import Order
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from .serializers import OrderSerializer
from bill.models import Bill
from .consumers import OrderConsumer
from table.models import Table
from table.serializers import TablewithorderdataSerializer

@receiver(post_save, sender = Order)
def create_update_order_signal(sender, instance, created, **kwargs):
    all_order_obj = Order.objects.exclude(id__in=Bill.objects.all().values("orders")).all()
    all_table_obj = Table.objects.all()
    OrderConsumer.external_group_send(room_name="waiter", content=TablewithorderdataSerializer(all_table_obj , many=True).data)
    OrderConsumer.external_group_send(room_name="manager", content=OrderSerializer(all_order_obj, many=True).data)
    OrderConsumer.external_group_send(room_name="bill_desk", content=TablewithorderdataSerializer(all_table_obj , many=True).data)

@receiver(pre_delete, sender=Order)
def delete_signal(sender, instance, using, **kwargs):
    all_order_obj = Order.objects.exclude(id__in=Bill.objects.all().values("orders")).all()
    all_table_obj = Table.objects.all()
    OrderConsumer.external_group_send(room_name="waiter", content=TablewithorderdataSerializer(all_table_obj , many=True).data)
    OrderConsumer.external_group_send(room_name="manager", content=OrderSerializer(all_order_obj, many=True).data)
    OrderConsumer.external_group_send(room_name="bill_desk", content=TablewithorderdataSerializer(all_table_obj , many=True).data)