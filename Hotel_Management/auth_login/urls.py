from django.urls import path
from .views import LoginView,Is_Login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('is_login/', Is_Login.as_view() , name='is_login'),
    path('login/', LoginView.as_view() , name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]