from .models import Order
from .serializers import (
    OrderSerializer,
    OrderCreateSerializer
)
from rest_framework import viewsets
from core.permissions import (
    IsAdmin,
    IsWaiter,
    IsManager
)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from rest_framework import permissions
from bill.models import Bill

# Create your views here.

class OrderManageView(viewsets.ModelViewSet):
    queryset = Order.objects.exclude(id__in=Bill.objects.all().values("orders")).all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin | IsWaiter | IsManager]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter
    ]
    filterset_fields  = {
        'status': ["exact"],
        'table__id': ["in"], 
        'item__id' : ["in"]
    }
    ordering_fields = ["id","category"]
    ordering = ["-created_at"]
    

    def get_permissions(self):
        if self.action in ["list","retrieve"]:
            self.permission_classes = [IsAdmin]
        if self.action in ["create","destroy"]:
            self.permission_classes = [IsAdmin | IsWaiter]
        return super(OrderManageView, self).get_permissions()
    
    def get_serializer_class(self):
        if self.action in ["create","update","partial_update"]:
            self.serializer_class = OrderCreateSerializer
        return super(OrderManageView, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        response_data = super(OrderManageView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All Order get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(OrderManageView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(OrderManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Order Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(OrderManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Order update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(OrderManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Order update Successfully!!!!")
        return Response(response.response)
    
    
    



