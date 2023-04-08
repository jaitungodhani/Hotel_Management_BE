from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import get_channel_layer
from .models import Order
from asgiref.sync import async_to_sync
from account.models import User
import json



class OrderConsumer(JsonWebsocketConsumer):

    def has_access_permission(self):
        try:
            # user_obj = User.objects.get(email=self.scope["user"])
            if self.scope["user"].role != self.room_name:
                if self.scope["user"].role != "admin":
                    return False
                else:
                    return True
            else:
                self.scope["room_name"] = self.scope["user"].role
                return True
        except Exception as e:
            return False
    
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)

        print("user_has_access_permission:-", self.has_access_permission())
        if self.has_access_permission():
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )

    @staticmethod
    def external_group_send(room_name, content):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(room_name), {"type": "order_message", "content": content}
        )
    
    def order_message(self, event):
        content = event["content"]
        self.send_json(content)