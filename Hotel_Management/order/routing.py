from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path("ws/order/<str:room_name>/", consumers.OrderConsumer.as_asgi()),
]
