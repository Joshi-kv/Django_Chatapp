import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()


#it accepts websocket connection from frontend

class chatConsumer(AsyncWebsocketConsumer):
    
    #it calls when websocket connection established.
    async def websocket_connect(self,event):
        print('connected',event)
        #accept established socket connection
        await self.accept()
        
    #it calls when message received.
    async def websocket_receive(self,event):
        print('received',event)
        
        #converting json string into python object
        received_message = json.loads(event['text']).get('message')
        print(received_message)
        
        if not received_message:
            return False
        response = {
            'message' : received_message
        }
        
        #sending message received on backend to frontend by converting python object into json string
        
        response_str = json.dumps(response)
        await self.send(response_str)
        
        
    #it calls when websocket disconnected.
    async def websocket_disconnect(self,event):
        print('disconnected',event)