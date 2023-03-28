from django.db import models
from Hotel_Management.behaviors import DateMixin
from django.utils.translation import gettext_lazy as _
from item.models import Item
from table.models import Table
import uuid

# Create your models here.

class Order(DateMixin, models.Model):
    STATUS_CHOICES = (
        ("Waiting", _("Waiting")),
        ("Prepairing", _("Prepairing")),
        ("Cooked", _("Cooked"))
    )

    id = models.UUIDField(
        verbose_name=_("id"),
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    table = models.ForeignKey(
        Table,
        verbose_name=_("table"),
        on_delete=models.DO_NOTHING,
        related_name="table_for_order"
    )
    item = models.ForeignKey(
        Item,
        verbose_name=_("item"),
        on_delete=models.DO_NOTHING,
        related_name="item_for_order"
    )
    quantity = models.IntegerField(
        verbose_name=_("quantity"),
        default=1
    )
    status = models.CharField(
        verbose_name=_("status"),
        choices=STATUS_CHOICES,
        default="Waiting",
        max_length=10
    )
    is_completed = models.BooleanField(
        verbose_name=_("is completed"),
        default=False
    )

    
    def __str__(self) -> str:
        return str(self.id) 
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
