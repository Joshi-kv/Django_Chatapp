from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    path('',views.index,name='index'),
    path('add-friends/',views.add_friend,name='addfriends')
]
