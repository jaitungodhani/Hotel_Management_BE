from django.shortcuts import render
from .models import Table
from .serializers import TableSerializer
from rest_framework import viewsets
from core.permissions import (
    IsAdmin,
    IsWaiter
)
from rest_framework import filters
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
# Create your views here.

class TableManageView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ["id","name"]
    ordering = ["name"]


    def list(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All User get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User update Successfully!!!!")
        return Response(response.response)
    


    




    
    