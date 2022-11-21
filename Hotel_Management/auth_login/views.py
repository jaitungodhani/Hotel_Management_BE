from django.test import TestCase
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
import utils_files.response_handler as rh
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        role=request.data.get("role")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if role==user.user_type:
                login(request,user)
                refresh_token=RefreshToken.for_user(user)
                user_data=UserSerializer(user)
                r=rh.ResponseMsg(data={
                    "access_token":str(refresh_token.access_token),
                    "refresh_token":str(refresh_token),
                    "user_data":user_data.data
                },error=False,msg="successfully login!!!!")
                return Response(r.response)
            else:
                r=rh.ResponseMsg(data={},error=True,msg="Invalid Credenticials!!!")
                return Response(r.response,status=status.HTTP_401_UNAUTHORIZED)
        r=rh.ResponseMsg(data={},error=True,msg="Invalid Credenticials!!!")
        return Response(r.response,status=status.HTTP_401_UNAUTHORIZED)

class Is_Login(APIView):
    def get(self, request, *args, **kwargs):
        data=request.user
        if data:
            serializer=UserSerializer(data)
            r=rh.ResponseMsg(data=serializer.data,error=False,msg="Login User data get successfully!!!")
            return Response(r.response)
        else:
            r=rh.ResponseMsg(data={},error=True,msg="Not login")
            return Response(r.response,status=status.HTTP_401_UNAUTHORIZED)
    

