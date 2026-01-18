from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
class Test(WebsocketConsumer):
    def connect(self):
        self.room_name = 'testroom'
        self.room_group_name = 'testgroup'
        
        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)

        self.accept()
        self.send(json.dumps({
            'title':'Connected'
        }))

    
    def receive(self, text_data = None, bytes_data = None):
        pass
    
    def disconnect(self, code):
          self.send(json.dumps({
            'title':'DisConnected'
        }))
          
    def send_student(self,event):
         print('HELLLLLOOOOOOO')
         print(json.dumps(event['data']))
         self.send(text_data=json.dumps(event['data']))

        