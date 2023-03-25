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
        password = validated_data.pop("password")
        user = super(UserCreateSerializer, self).create(validated_data)
        group = get_object_or_404(Group, name__iexact=role)
        user.groups.add(group)
        user.set_password(password)
        user.save()
        return user
    
    def to_representation(self, instance):
        return UserSerializer(instance).data


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "last_login",
            "password",
            "is_superuser",
            "is_staff",
            "is_active"
        )

    def to_representation(self, instance):
        return UserSerializer(instance).data
    

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, required = True)
    new_password = serializers.CharField(max_length=100, required = True)
    confirm_password = serializers.CharField(max_length=100, required = True)

    def validate(self, attrs):
        self.password = attrs["password"]
        self.request = self.context.get("request")

        if not self.request.user.check_password(self.password):
            raise serializers.ValidationError("Password is Not Valid!!!")
        
        self.new_password = attrs["new_password"]
        self.confirm_new_password = attrs["confirm_password"]

        if self.new_password != self.confirm_new_password:
            raise serializers.ValidationError("Please, Add both password same")
        
        return super(ResetPasswordSerializer,self).validate(attrs)
    
    def set_password(self):
    
        self.request.user.set_password(
           self.new_password
        )
        self.request.user.save()