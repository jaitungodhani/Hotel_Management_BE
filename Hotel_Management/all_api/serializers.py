from dataclasses import fields
from pyexpat import model
from .models import *
from rest_framework.serializers import ModelSerializer

class TableSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"