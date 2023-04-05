from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from User.models import Profile
# Create your views here.
@login_required(login_url='User:login')
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {
        "user_profile":user_profile
    }
    return render(request,'index.html',context)