from .models import Bill
from .serializers import (
    BillSerializer,
    BillCreateSerializer
)
from rest_framework import viewsets
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from core.permissions import (
    IsBillDesk,
    IsAdmin
)
from rest_framework import filters
from rest_framework.decorators import action
# Create your views here.


class BillManageView(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsBillDesk | IsAdmin]
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ["id","category"]
    ordering = ["-created_at"]
    

    def get_serializer_class(self):
        if self.action in ["create","update","partial_update"]:
            self.serializer_class = BillCreateSerializer
        return super(BillManageView, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All Bill get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Bill Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Bill update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Bill update Successfully!!!!")
        return Response(response.response)
    

    
        
