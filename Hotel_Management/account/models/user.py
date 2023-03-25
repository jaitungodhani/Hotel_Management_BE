from .user_manager import CustomUserManager
from Hotel_Management.behaviors import DateMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractBaseUser, DateMixin, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email Address"), 
        unique=True
        )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("Is Staff"),
        default=False
    )
    phone = models.CharField(
        verbose_name=_("Phone No"),
        max_length=13
    )
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=100
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username']

    objects = CustomUserManager()

    class Meta:
        ordering = ('id',)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email + " ---- " + str(self.pk)
    

    @property
    def role(self):
        group = self.groups.first()
        return group.name if group else None