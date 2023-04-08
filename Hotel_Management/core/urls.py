from django.urls import path
from .views import waiter, manager, bill_desk


urlpatterns = [
    path("core/waiter/", waiter),
    path("core/manager/", manager),
    path("core/bill_desk/", bill_desk)
]
