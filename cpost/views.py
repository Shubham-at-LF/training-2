"""tell us about the views """

from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.


def index(request) :
    "jkhfjkshdka"
    context ={}
   
    if request.method == "POST" :
        Name = request.POST['UserName']
        new_user = user(name = Name, profilePic = "adf")
        new_user.save()
    
    return render(request, "cpost/index.html", context)

def add(request):
        userProfile = str(request.GET["Userpicture"])
        return  HttpResponse("Your picture id" + "" + userProfile)