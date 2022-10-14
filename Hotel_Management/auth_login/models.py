from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# class UserManager(BaseUserManager):
#     def create_user(self, username, password,email):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('Users must have an username and email')

#         user = self.model(
#             username=username,
#             email=email
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, username, password,email):
#         """
#         Creates and saves a staff user with the given email and password.
#         """

#         if not username:
#             raise ValueError('staff user must have an username and email')

#         user = self.model(
#             username=username,
#             email=email
#         )

#         user.set_password(password)
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email,password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         if not username and not email:
#             raise ValueError('superuser must have an username and email')

#         user = self.model(
#             username=username,
#             email=email
#         )

#         user.set_password(password)
#         user.is_staff=True
#         user.is_manager=True
#         user.is_owner = True
#         user.save(using=self._db)
#         return user




class User(AbstractUser):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'Hotel_management_profile/' + filename

    USER_TYPE_CHOICES = (
      ('waiter', 'waiter'),
      ('manager', 'manager'),
      ('billdesk', 'billdesk'),
      ('admin', 'admin'),
    )
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
    user_type = models.CharField(choices=USER_TYPE_CHOICES,max_length=100,default="waiter")

   