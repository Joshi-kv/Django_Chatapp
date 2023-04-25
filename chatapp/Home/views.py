
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from User.models import Profile,User
from . models import ChatMessage

# Create your views here.
@login_required(login_url='User:login')
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    friends = Profile.objects.exclude(user=request.user)

    context = {
        "user_profile": user_profile,
        "friends": friends,


    }
    return render(request,'index.html',context)



def chat_page(request,username):
    user_obj = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_obj)
    current_user = Profile.objects.get(user=request.user)

    
    #fetching messages saved on db using thread name
    if request.user.id > user_obj.id :
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else :
        thread_name = f'chat_{user_obj.id}-{request.user.id} '
    
    messages = ChatMessage.objects.filter(thread_name=thread_name)

    
    context = {

        'user_obj':user_obj,
        'user_profile':user_profile,
        'messages' : messages,
        'current_user' : current_user,

        
    }
    return render(request,'chat_page.html',context)