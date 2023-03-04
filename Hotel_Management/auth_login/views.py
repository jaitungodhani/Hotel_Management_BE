
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import utils_files.response_handler as rh
from rest_framework import status
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)
from .serializers import (
    LoginSerializer,
    UserSerializer,
    PermissionSerializer
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.contrib.auth.models import (
    Permission
)
from .permissions import (
    IsAdmin
)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        r=rh.ResponseMsg(data=serializer.validated_data,error=False,msg="User Login Successfully!!!")
        return Response(r.response)


class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = rh.ResponseMsg(serializer.validated_data, False, "Access Token Get Successfully!!!")
        return Response(status=status.HTTP_200_OK, data=response.response)

class Is_Login(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        response = rh.ResponseMsg(serializer.data, False, "User information get Successfully!!!")
        return Response(status=status.HTTP_200_OK, data=response.response)
    

class PermissionView(ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request, *args, **kwargs):
        queryset = Permission.objects.all().order_by("id")
        serializer = PermissionSerializer(queryset, many=True)
        response = rh.ResponseMsg(serializer.data, False, "Permissions get Successfully!!!")
        return Response(status=status.HTTP_200_OK, data=response.response)
