from django.db import models
from Hotel_Management.behaviors import DateMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(DateMixin, models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Category Name"),
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name