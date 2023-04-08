from order.models import Order
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from order.serializers import OrderSerializer
from bill.models import Bill
from order.consumers import OrderConsumer
from table.models import Table
from table.serializers import TablewithorderdataSerializer
from .serializers import BillSerializer

@receiver(post_save, sender = Bill)
def create_update_bill_signal(sender, instance, created, **kwargs):
    all_table_obj = Table.objects.all()
    OrderConsumer.external_group_send(room_name="waiter", content=TablewithorderdataSerializer(all_table_obj , many=True).data)
    OrderConsumer.external_group_send(room_name="manager", content=OrderSerializer(Order.objects.exclude(id__in=Bill.objects.values("orders")), many=True).data)
    OrderConsumer.external_group_send(room_name="bill_desk", content={"type": "current_bill", "data":TablewithorderdataSerializer(all_table_obj , many=True).data})
    OrderConsumer.external_group_send(room_name="bill_desk", content={"type": "paid_bill", "data":BillSerializer(Bill.objects.all() , many=True).data})

@receiver(post_delete, sender=Bill)
def delete_bill_signal(sender, instance, using, **kwargs):
    all_order_obj = Order.objects.exclude(id__in=Bill.objects.all().values("orders")).all()
    all_table_obj = Table.objects.all()
    OrderConsumer.external_group_send(room_name="waiter", content=TablewithorderdataSerializer(all_table_obj , many=True).data)
    OrderConsumer.external_group_send(room_name="manager", content=OrderSerializer(all_order_obj, many=True).data)
    OrderConsumer.external_group_send(room_name="bill_desk", content={"type": "current_bill", "data":TablewithorderdataSerializer(all_table_obj , many=True).data})
    OrderConsumer.external_group_send(room_name="bill_desk", content={"type": "paid_bill", "data":BillSerializer(Bill.objects.all(), many=True).data})