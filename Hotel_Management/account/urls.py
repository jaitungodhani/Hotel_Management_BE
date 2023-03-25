from django.urls import path, include
from .views import (
    LoginView,
    RefreshView,
    ManageUserView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("usermanage", ManageUserView)

urlpatterns = [
    path('', include(router.urls)),
    path("login/", LoginView.as_view()),
    path("refresh/", RefreshView.as_view()),
]
