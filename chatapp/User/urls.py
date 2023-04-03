from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('signup',views.signup,name='signup')
]
