from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import Profile
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

