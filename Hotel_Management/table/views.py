from django.shortcuts import render
from .models import Table
from .serializers import (
    TableSerializer,
    TablewithorderdataSerializer
)
from rest_framework import viewsets
from core.permissions import (
    IsAdmin,
    IsWaiter,
    IsBillDesk
)
from rest_framework import filters
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from rest_framework.decorators import action
import qrcode
from PIL import Image
import base64
from io import BytesIO
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class TableManageView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ["id","name"]
    ordering = ["name"]
    permission_classes = [IsAdmin]


    def list(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All Table get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Table Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Table update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(TableManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Table update Successfully!!!!")
        return Response(response.response)
    

    @action(
        methods=["get"],
        detail=False,
        permission_classes = [IsWaiter | IsAdmin | IsBillDesk]
    )
    def tabledata_with_order_data(self, request):
        serializer = TablewithorderdataSerializer(self.get_queryset(), many=True)
        response = ResponseMsg(error=False, data=serializer.data, message="Get Table data Successfully!!!!")
        return Response(response.response)
    

    # @action(
    #     methods=["get"],
    #     detail=False,
    #     permission_classes = [IsBillDesk | IsAdmin]
    # )
    # def tableBillData(self, request):
    #     serializer = TablewithoBilldataSerializer(self.get_queryset(), many=True)
    #     response = ResponseMsg(error=False, data=serializer.data, message="Get Table data Successfully!!!!")
    #     return Response(response.response)
    

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='table_id',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
                description='Table Id'
            )
        ]
    )
    @action(
        methods=["get"],
        detail=False,
        permission_classes=[IsAdmin | IsBillDesk]
    )
    def table_base_bill_qrcode(self, request):
        table_id = request.query_params.get("table_id", None)
        if not table_id:
            raise Exception("Please pass table_id")
        try:
            table_obj = Table.objects.get(id = table_id)
        except Table.DoesNotExist:
            raise Exception("table not exist, please check")
        serializer = TablewithorderdataSerializer(table_obj)

        height = 250
        width = 250
        

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # L -> M -> Q -> H
            box_size=4,
            border=2,
        )

        # qr.add_data('upi://pay?pa='+upi_id +
        #             '&pn='+str(name_ac)+'&am='+str(amount)+'&cu=INR')

        qr.add_data('upi://pay?pa=jaitungodhani229@oksbi&pn=jaitun&am='+str(serializer.data["total_amount"])+'&cu=INR')

        qr.make(fit=str(height)+'x'+str(width))

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
       
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        response = ResponseMsg(error=False, data=f"data:file/png;base64,{img_str}", message="get data Successfully!!!!")
        return Response(response.response)
        
    




    




    
    