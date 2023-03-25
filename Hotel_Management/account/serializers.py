from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group

User = get_user_model()


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_data"] = {
            "id" : self.user.id,
            "email":self.user.email,
            "username":self.user.username
        }
        return data
    

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions"
        )
        

    def get_role(self, obj):
        return obj.role



class UserCreateSerializer(serializers.ModelSerializer):
    USER_ROLE_CHOICES = (
        ("Waiter", _("Waiter")),
        ("Manager", _("Manager")),
        ("Bill Desk", _("Bill Desk")),
        ("Admin", _("Admin"))
    )

    role = serializers.ChoiceField(choices=USER_ROLE_CHOICES, write_only = True, required=True)

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "last_login"
        )

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = super(UserCreateSerializer, self).create(validated_data)
        group = get_object_or_404(Group, name__iexact=role)
        user.groups.add(group)
        user.save()
        return user
    
    def to_representation(self, instance):
        return UserSerializer(instance).data