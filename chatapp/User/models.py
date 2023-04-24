from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True,default="no-user.png")
    # friends = models.ManyToManyField("Friend",related_name="friend_profile") 

    
    def __str__(self):
        return f'{self.user.username}'
    
# class Friend(models.Model):
#     profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'{self.profile.user}'