from django.test import TestCase
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
import utils_files.response_handler as rh
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            refresh_token=RefreshToken.for_user(user)
            user_data=UserSerializer(user)
            r=rh.ResponseMsg(data={
                "access_token":str(refresh_token.access_token),
                "refresh_token":str(refresh_token),
                "user_data":user_data.data
            },error=False,msg="successfully login!!!!")
            return Response(r.response)
        r=rh.ResponseMsg(data={},error=True,msg="Invalid Credenticials!!!")
        return Response(r.response,status=status.HTTP_401_UNAUTHORIZED)

# class LoginView(TokenObtainPairView):
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         response.data['custom_key'] =  'my_custom_data'
#         r=rh.ResponseMsg(data=response.data,error=False,msg="successfully login!!!!")
#         return Response(r.response)
        