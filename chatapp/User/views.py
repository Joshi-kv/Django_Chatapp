from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='User:signup')
def signup(request):
    return render(request,'signup.html')
