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
    path('account/', include(router.urls)),
    path("account/login/", LoginView.as_view()),
    path("account/refresh/", RefreshView.as_view()),
]

