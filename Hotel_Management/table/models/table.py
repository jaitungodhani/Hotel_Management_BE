from django.db import models
from Hotel_Management.behaviors import DateMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Table(DateMixin, models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Table Name"),
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = _("Table")
        verbose_name_plural = _("Tables")

    def __str__(self) -> str:
        return self.name