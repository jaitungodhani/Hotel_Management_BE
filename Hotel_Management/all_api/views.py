from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import TableSerializer
from .models import Table
import utils_files.response_handler as rh
from rest_framework.response import Response
# Create your views here.

class TableView(ViewSet):
    def list(self,request,format=None):
        all_table_obj=Table.objects.all()
        serilaize_data=TableSerializer(all_table_obj,many=True)
        r=rh.ResponseMsg(data=serilaize_data.data,error=False,msg="Get Successfully!!!")
        return Response(r.response)


