from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    path('',views.index,name='index'),
    # path('friends-list',views.friend_list,name='friendslist'),
    # path('add-friends/<int:friend_id>/',views.add_friend,name='addfriends'),
    path('chat/<str:username>/', views.chat_page, name='chat')

     
]
