from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
import uuid


class UserManager(BaseUserManager):
    def create_user(self, username, password,email):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username and email')

        user = self.model(
            username=username,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password,email):
        """
        Creates and saves a staff user with the given email and password.
        """

        if not username:
            raise ValueError('staff user must have an username and email')

        user = self.model(
            username=username,
            email=email
        )

        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,password):
        """
        Creates and saves a superuser with the given email and password.
        """
        if not username and not email:
            raise ValueError('superuser must have an username and email')

        user = self.model(
            username=username,
            email=email
        )

        user.set_password(password)
        user.is_staff=True
        user.is_manager=True
        user.is_owner = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    def get_avatar_path(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return 'Hotel_management_profile/' + filename

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
    date_joined=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False) # a admin user; non super-user
    is_owner = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password'] # Email & Password are required by default.
    objects = UserManager()

    def get_pre_signed_url(self):
        return self.profile_picture

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    