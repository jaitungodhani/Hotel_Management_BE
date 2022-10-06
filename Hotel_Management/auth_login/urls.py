from django.urls import path
from .views import LoginView
urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    # path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]