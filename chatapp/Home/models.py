from django.db import models
from User.models import Profile
# Create your models here.

#model to save messages

class ChatMessage(models.Model) :
    sender = models.CharField(max_length=250,default=None)
    message = models.TextField(null=True,blank=True)
    thread_name = models.CharField(max_length=100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) :
        return f'{self.message} from {self.sender}'