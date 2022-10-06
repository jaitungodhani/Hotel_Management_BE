from enum import unique
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Table(models.Model):
    name=models.CharField(max_length=400,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="table"
        verbose_name_plural="tables"

# class Category(models.Model):
#     name=models.CharField(max_length=255,unique=True)

#     def __str__(self):
#         return 