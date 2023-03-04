from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("The Username must be set"))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(username, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'Hotel_management_profile/' + filename

    # USER_TYPE_CHOICES = (
    #   ('waiter', 'waiter'),
    #   ('manager', 'manager'),
    #   ('billdesk', 'billdesk'),
    #   ('admin', 'admin'),
    # )
    username=models.CharField(max_length=100, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name=models.CharField(null=True,blank=True, max_length=100)
    last_name=models.CharField(null=True, blank=True, max_length=100)
    profile_picture=models.ImageField(upload_to=get_avatar_path, null=True, blank=True)
    phone_number=models.PositiveBigIntegerField(default=8511192040)
    # user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=100,default="waiter")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def role(self):
        group = self.groups.first()
        return group.name if group else None