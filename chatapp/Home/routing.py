from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('chat/<int:friend_id>/',consumers.chatConsumer.as_asgi()),
]