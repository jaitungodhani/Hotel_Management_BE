from django.db import models
from Hotel_Management.behaviors import (
    DateMixin
)
from django.contrib.auth import get_user_model

User = get_user_model()


class ForgotpasswordToken(DateMixin, models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    token = models.CharField(
        max_length=100
    )

    def __str__(self) -> str:
        return self.token + '----' + str(self.user.id)
    

    class Meta:
        ordering = ("id",)
        verbose_name = "ForgotPasswordToken"
        verbose_name_plural = "ForgotPasswordTokens"