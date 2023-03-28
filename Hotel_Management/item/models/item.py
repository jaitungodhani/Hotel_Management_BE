from django.db import models
from Hotel_Management.behaviors import DateMixin
from django.utils.translation import gettext_lazy as _
from category.models import Category


# Create your models here.

class Item(DateMixin, models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Item Name")
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        decimal_places=2,
        max_digits=10
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        related_name="category_for_item",
        on_delete=models.CASCADE
    )


    class Meta:
        ordering = ("name",)
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        unique_together = ('name', 'category',)

    def __str__(self) -> str:
        return self.name