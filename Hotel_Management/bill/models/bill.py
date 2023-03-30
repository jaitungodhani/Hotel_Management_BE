from django.db import models
from Hotel_Management.behaviors import DateMixin
from django.utils.translation import gettext_lazy as _
from order.models import Order
from table.models import Table
import uuid


# Create your models here.


class Bill(DateMixin, models.Model):

    PAYMENT_TYPE = (
        ("By Cash", _("By Cash")),
        ("By UPI", _("By UPI"))
    )


    id = models.UUIDField(
        verbose_name=_("id"),
        primary_key=True,
        default=uuid.uuid4
    )
    table = models.ForeignKey(
        Table,
        verbose_name=_("table"),
        on_delete=models.CASCADE
    )
    total_amount = models.DecimalField(
        verbose_name=_("total amount"),
        decimal_places=2,
        max_digits=10
    )
    orders = models.ManyToManyField(
        Order,
        verbose_name=_("orders"),
        related_name="orders_for_bill"
    )
    payment_type = models.CharField(
        verbose_name=_("Payment Type"),
        max_length=25,
        default="By Cash"
    )

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Bill")
        verbose_name_plural = _("Bills")

