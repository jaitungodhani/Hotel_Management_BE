from rest_framework import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserCreateSerializer
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)
from utils.response_handler import ResponseMsg
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from core.permissions import (
    IsAdmin
)
# Create your views here.

User = get_user_model()

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
        if self.action in ["create","delete"]:
            self.permission_classes = [IsAdmin]
        return super(ManageUserView, self).get_permissions()
    
    def get_serializer_class(self):
        if self.action in ["create"]:
            self.serializer_class = UserCreateSerializer
        return super(ManageUserView, self).get_serializer_class()
