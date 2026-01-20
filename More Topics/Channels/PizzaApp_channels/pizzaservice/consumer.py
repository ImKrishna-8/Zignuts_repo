from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Order
class PizzaUpdates(WebsocketConsumer):
    def connect(self):
        self.order_id = self.scope['url_route']['kwargs']['order_id']
        self.room_group_name = f'order_{self.order_id}'

        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
        self.accept()
        order = Order.objects.get(id=self.order_id)
        self.send(text_data=json.dumps({
                "status": order.status
        }))

        
    def receive(self, text_data = None, bytes_data = None):
        pass
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def update_status(self,event):
        self.send(text_data=json.dumps({
            'status':event['status']
        }))