from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#model to save messages

class ChatMessage(models.Model) :
    sender = models.CharField(max_length=250,default=None)
    message = models.TextField(null=True,blank=True)
    thread_name = models.CharField(max_length=100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return f'{self.message} from {self.sender}'
    
    
#model for chat notification
class Notification(models.Model):
    chat = models.ForeignKey(to=ChatMessage,on_delete=models.CASCADE)
    sender = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='receiver')
    is_seen = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.chat} from {self.sender} to {self.receiver}'