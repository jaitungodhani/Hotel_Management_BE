from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }