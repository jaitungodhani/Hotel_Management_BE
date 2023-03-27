from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .models import (
    ForgotpasswordToken
)
import uuid
from Hotel_Management.celery import send_mail

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
        self.password = validated_data.pop("password")
        self.email = validated_data.pop("email")
        user = super(UserCreateSerializer, self).create(validated_data)
        group = get_object_or_404(Group, name__iexact=role)
        user.groups.add(group)
        user.set_password(self.password)
        user.save()
        self.send_mail()
        return user
    
    def send_mail(self):
        subject = "Welcome to Hotel Management Service !!!!"
        message = (
            f"Hello\n\n"
            f"Hotel Management Service Created account for"
            f" this email {self.email}.\n\n"
            f"Below we have mention your password\n"
            f"{self.password} \n\n\n\n"
            f" And we have request you to please reset your new password by using this password for further use"
            f"\n"
            f"If you did not make this request, please contact us at"
            f" hotelmanagement@gmail.com\n\n"
            f"-- Hotel Managent Service 😊😊"
        )
        send_mail.apply_async(
            args=[subject, message, self.email],
        )

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


class ForgotPassEmailSendSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)

    def validate(self, attrs):
        self.email = attrs["email"]

        try:
            self.user = User.objects.get(email = self.email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Email is Wrong, Please check !!!!")
        
        return super(ForgotPassEmailSendSerializer, self).validate(attrs)
    
    def send_mail(self):
        user_obj_token = ForgotpasswordToken.objects.filter(user__email=self.user.email).first()
        token=str(uuid.uuid4())

        if user_obj_token:
            user_obj_token.token = token
            user_obj_token.save()
        else:
            ForgotpasswordToken.objects.create(user = self.user, token = token)

        domain="127.0.0.1:3000"
        subject = "Reset your Hotel Management password"
        message = (
            f"Hello\n\n"
            f"We've received a request to reset the password for the"
            f" Hotel Management account associated with {self.email}.\n\n"
            f"Please use this link to reset your password\n"
            f"{domain}/api/change_password/{token}"
            f"\n"
            f"If you did not make this request, please contact us at"
            f" hotelmanagement@gmail.com\n\n"
            f"-- Hotel Managent Service 😊😊"
        )

        send_mail.apply_async(
            args=[subject, message, self.email],
        )

class ForgotpasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100, required=True)
    new_password = serializers.CharField(max_length=100, required = True)
    confirm_password = serializers.CharField(max_length=100, required = True)

    def validate(self, attrs):
        self.token = attrs["token"]

        try:
            self.forgot_password_token_obj = ForgotpasswordToken.objects.get(token = self.token)
        except ForgotpasswordToken.DoesNotExist:
            raise serializers.ValidationError("Token Not Valid!!!")
        
        
        self.new_password = attrs["new_password"]
        self.confirm_new_password = attrs["confirm_password"]

        if self.new_password != self.confirm_new_password:
            raise serializers.ValidationError("Please, Add both password same")
        
        return super(ForgotpasswordSerializer,self).validate(attrs)
    
    def set_password(self):
    
        self.forgot_password_token_obj.user.set_password(
           self.new_password
        )
        self.forgot_password_token_obj.user.save()
        self.forgot_password_token_obj.delete()