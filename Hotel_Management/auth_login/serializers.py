from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    Permission
)
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
User=get_user_model()


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_data"] = {
            "user_id":self.user.id,
            "user_name":self.user.username,
            "role":self.user.role
        }
        return data


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions"
        )

    def get_role(self,obj):
        group = obj.groups.first()
        return group.name if group else None
    

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission
        fields="__all__"