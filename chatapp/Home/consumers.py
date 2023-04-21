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
        
        #fetching users id 
        
        current_user_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        
        #creating chat room using users id
        
        if int(current_user_id) > int(other_user_id) :
            self.room_name = f'{current_user_id}-{other_user_id}'
        else :
            self.room_name = f'{other_user_id}-{current_user_id}'
            
        print(self.room_name)
        
        self.room_group_name = f'chat_{self.room_name}'
        
        #adding group to channel layers
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
                    
        #accept established socket connection
        await self.accept()
        
    #it calls when message received.
    async def websocket_receive(self,event):
        print('received',event)
        
        
    #it calls when websocket disconnected.
    async def websocket_disconnect(self,event):
        print('disconnected',event)
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )