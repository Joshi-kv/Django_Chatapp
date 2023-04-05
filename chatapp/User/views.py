from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import Profile
# Create your views here.


def signup(request):
    if request.method == 'POST':  
        username = request.POST['username']  
        email = request.POST['email']  
        password = request.POST['password']  
        confirm_password = request.POST['confirm_password']  
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists() :
                messages.info(request,'Email Already Taken')
                return redirect("User:signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect("User:signup")
            else :
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                user_model = User.objects.get(username=username)
                profile = Profile.objects.create(user = user_model)
                profile.save()
                return redirect("User:login")
        else:
            messages.info(request,'Password Not Match')
            return redirect('User:signup')
        
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None :
            auth.login(request,user)
            return redirect('Home:index')
        else : 
            messages.info(request,"Invalid Credentials")
            return redirect('User:login')
    return render(request,'login.html')


def logout(request) :
    auth.logout(request)
    return redirect('User:login')

def settings(request) :
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST" :
        image = request.FILES.get('profile')
        user_profile.profile_pic = image
        user_profile.save()
    context = {
        'user_profile':user_profile
    }
    return render(request,'settings.html',context)