from email.policy import default
from enum import auto, unique
from secrets import choice
from statistics import mode
from tabnanny import verbose
from unicodedata import category
import uuid
from django.db import models

# Create your models here.
class Table(models.Model):
    name=models.CharField(max_length=400,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="table"
        verbose_name_plural="tables"

class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"

class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Item"
        verbose_name_plural="Items"
        unique_together = ('category_id', 'name',)

class Order(models.Model):
    STATUS_CHOICES = (
        ('Waiting', 'Waiting'),
        ('Processing', 'Processing'),
        ('Completed','Completed')
    )

    id=models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
    Item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    table=models.ForeignKey(Table,related_name="order",on_delete=models.CASCADE)
    status=models.CharField(choices=STATUS_CHOICES,max_length=255,default="Waiting")
    create_at=models.DateTimeField(auto_now=True)
    pay=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"

class Bill(models.Model):
    id=models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    total_amount=models.IntegerField()
    pay=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name="bill"
        verbose_name_plural="bills"
