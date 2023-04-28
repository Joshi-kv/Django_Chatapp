from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('chat/<int:id>/',consumers.chatConsumer.as_asgi()),
    path('online/',consumers.OnlineStatusConsumer.as_asgi()),
    path('notification/',consumers.NotificationConsumer.as_asgi()),
    
]