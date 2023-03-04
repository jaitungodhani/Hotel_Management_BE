from django.urls import path,include
from .views import LoginView,Is_Login,RefreshTokenView, PermissionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("permissionview", PermissionView, basename="permissionview")

urlpatterns = [
    path('', include(router.urls)),
    path('is_login/', Is_Login.as_view() , name='is_login'),
    path('login/', LoginView.as_view() , name='token_obtain_pair'),
    path('refresh_token/', RefreshTokenView.as_view(), name='token_refresh'),
]