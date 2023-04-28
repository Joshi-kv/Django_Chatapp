from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
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
class ChatNotification(models.Model):
    chat = models.ForeignKey(to=ChatMessage,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}'