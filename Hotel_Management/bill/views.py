from .models import Bill
from .serializers import (
    BillSerializer,
    BillCreateSerializer
)
from rest_framework import viewsets
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from django.http import HttpResponse
from core.permissions import (
    IsBillDesk,
    IsAdmin
)
from rest_framework import filters
from .pdf_generator import BillPdfGenerator
from reportlab.platypus import Paragraph
from datetime import datetime

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
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Hotel_Management_online_bill.pdf"'
        col_width = [60,190,110,170]
        table_header = [Paragraph('Index'), Paragraph('Item'), Paragraph('Quan.'), Paragraph('Amount')]
        table_data = []
        for i,data in enumerate(response_data.data["orders"]):
            table_data.append([i+1, data["item"]["name"],"x " + str(data["quantity"]), data["quantity"] * float(data["item"]["price"])])
        table_data.append([None,None,"CGST :- ", 0.0])
        table_data.append([None,None,"CGST :- ", 0.0])
        table_data.append([None,None,"Total Amount :- ", str(response_data.data["total_amount"]) + " Rs."])
        bill_data = {
            "bill_no":response_data.data["id"],
            "date_time": str(datetime.today())
        }
        response = BillPdfGenerator(bill_data, table_data, table_header, col_width, response)
        return response.main()
    
    def create(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=response_data.data, data=response_data.data, message="Bill update Successfuly!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Bill update Successfuly!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(BillManageView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Bill update Successfully!!!!")
        return Response(response.response)
    

    
        
