from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Item
from .serializers import (
    ItemSerializer,
    ItemCreateSerializer
)
from rest_framework import viewsets
from core.permissions import (
    IsAdmin,
    IsWaiter
)
from rest_framework import filters
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.

class ItemManageView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    permission_classes = [IsAdmin]
    ordering_fields = ["id","name"]
    ordering = ["created_at"]

    def get_serializer_class(self):
        if self.action in ["create","update","partial_update"]:
            self.serializer_class = ItemCreateSerializer
        return super(ItemManageView, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        response_data = super(ItemManageView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All Item get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(ItemManageView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(ItemManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Item Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(ItemManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Item update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(ItemManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Item update Successfully!!!!")
        return Response(response.response)
    


    




    
    