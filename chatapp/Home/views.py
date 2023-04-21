from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from User.models import Profile,Friend,User
from django.db.models import Subquery, OuterRef
# Create your views here.
@login_required(login_url='User:login')
def index(request):
    user_profile = Profile.objects.get(user=request.user)

    friends = user_profile.friends.all()
    context = {
        "user_profile": user_profile,

        "friends": friends,
    }
    return render(request,'index.html',context)

def friend_list(request):
    user_profile = Profile.objects.get(user=request.user)
    friends = Profile.objects.exclude(user=request.user)
    
    context = {
        "user_profile":user_profile,
        "friends":friends
    }
    return render(request,'addfriend.html',context)

def add_friend(request, friend_id):
    # Get the current user's Profile object
    user_profile = Profile.objects.get(user=request.user)
    # Get the Profile object for the friend to be added
    friend_profile = Profile.objects.get(id=friend_id)
    # Check if the friend is already in the current user's friend list
    if user_profile.friends.filter(profile=friend_profile).exists():
        return JsonResponse({"success": True, "message": "Already your friend"})
    else:
        # Create a new Friend object for the friend to be added
        new_friend = Friend.objects.create(profile=friend_profile)
        # Add the new Friend object to the current user's friends list
        user_profile.friends.add(new_friend)
        # Redirect to the home page
        return JsonResponse({"success": True})


def chat_page(request,username):
    user_obj = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_obj)
    context = {

        'user_obj':user_obj,
        'user_profile':user_profile
    }
    return render(request,'chat_page.html',context)