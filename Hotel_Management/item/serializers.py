from rest_framework import serializers
from .models import (
    Item
)
from category.serializers import CategorySerializer


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)

    class Meta:
        model = Item
        fields = "__all__"


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def to_representation(self, instance):
        return ItemSerializer(instance).data