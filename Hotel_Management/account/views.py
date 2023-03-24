from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .serializers import (
    LoginSerializer
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
# Create your views here.


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        response_data = super(LoginView, self).post(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Login Successfully!!!!")
        return Response(response.response)

class RefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        response_data = super(RefreshView, self).post(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Access Token get Successfully!!!!")
        return Response(response.response)