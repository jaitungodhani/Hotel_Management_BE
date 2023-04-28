from rest_framework import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    ResetPasswordSerializer,
    ForgotPassEmailSendSerializer,
    ForgotpasswordSerializer
    )
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from core.permissions import (
    IsAdmin,
    IsUserItSelf
)
from rest_framework import permissions
from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()


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
    

class ManageUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["create","destroy","list"]:
            self.permission_classes = [IsAdmin]
        if self.action in ["update","retrieve","partial_update"]:
            self.permission_classes = [IsAdmin | IsUserItSelf]
        return super(ManageUserView, self).get_permissions()
    
    def get_serializer_class(self):
        if self.action in ["create"]:
            self.serializer_class = UserCreateSerializer
        if self.action in ["update","partial_update"]:
            self.serializer_class = UserUpdateSerializer
        return super(ManageUserView, self).get_serializer_class()
    
    def list(self, request, *args, **kwargs):
        response_data = super(ManageUserView, self).list(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="All User get Successfully!!!!")
        return Response(response.response)
    
    def retrieve(self, request, *args, **kwargs):
        response_data = super(ManageUserView, self).retrieve(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="Data Get Successfully!!!!")
        return Response(response.response)
    
    def create(self, request, *args, **kwargs):
        response_data = super(ManageUserView, self).create(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User Create Successfully!!!!")
        return Response(response.response)
    
    def update(self, request, *args, **kwargs):
        response_data = super(ManageUserView, self).update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User update Successfully!!!!")
        return Response(response.response)
    
    def partial_update(self, request, *args, **kwargs):
        response_data = super(ManageUserView, self).partial_update(request, *args, **kwargs)
        response = ResponseMsg(error=False, data=response_data.data, message="User update Successfully!!!!")
        return Response(response.response)
    
    @swagger_auto_schema(
        method="post",
        request_body=ResetPasswordSerializer
    )
    @action(
        methods=["POST"],
        detail=False,
        serializer_class = ResetPasswordSerializer
    )
    def reset_password(self, request):
        serializer = ResetPasswordSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_password()
        response = ResponseMsg(error=False, data={}, message="Password Reset Successfully!!!!")
        return Response(response.response)
    

    @swagger_auto_schema(
        method="post",
        request_body=ForgotPassEmailSendSerializer
    )
    @action(
        methods=["POST"],
        detail=False,
        serializer_class = ForgotPassEmailSendSerializer,
        permission_classes = [permissions.AllowAny]
    )
    def forgot_password_send_mail(self, request):
        serializer = ForgotPassEmailSendSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_mail()
        response = ResponseMsg(error=False, data={}, message="Email Sent Successfully!!!!")
        return Response(response.response)
    

    @swagger_auto_schema(
        method="post",
        request_body=ForgotpasswordSerializer
    )
    @action(
        methods=["POST"],
        detail=False,
        serializer_class = ForgotpasswordSerializer,
        permission_classes = [permissions.AllowAny]
    )
    def forgot_password(self, request):
        serializer = ForgotpasswordSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_password()
        response = ResponseMsg(error=False, data={}, message="Password set Successfully!!!!")
        return Response(response.response)



    
