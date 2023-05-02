from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import Profile
from .models import Notification
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#signal to notify online status

@receiver(post_save, sender=Profile)
def send_online_status(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        user = instance.user.username
        online_status = instance.is_online

        data = {
            'username':user,
            'online_status':online_status,
        }
        async_to_sync(channel_layer.group_send)(
            'user', {
                'type':'send_online_status',
                'value':json.dumps(data)
            }
        )

#signals for notification 

@receiver(post_save,sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created :
        channel_layer = get_channel_layer()
        notification_count = Notification.objects.filter(is_seen=False,sender=instance.sender,receiver=instance.receiver).count()
        user_id = f'{instance.receiver.id}'
        receiver = instance.receiver.username
        sender = instance.sender.username
        seen = instance.is_seen
        
        data = {
            'notification_count':notification_count,
            'receiver':receiver,
            'sender' : sender,
            'seen':seen,
        }
        

     
        async_to_sync(channel_layer.group_send)(
            user_id,
            {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )