from django.contrib import admin
from . models import ChatMessage,ChatNotification
# Register your models here.

admin.site.register([ChatMessage,ChatNotification]) 

