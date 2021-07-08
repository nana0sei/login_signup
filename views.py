from django.shortcuts import render
import datetime
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from attendanceapp.emailBackend import emailBackend
from attendanceapp.models import CustomUser
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def showDemoPage(request):
    return render(request, "demo.html")

def showLoginPage(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h1>Method Not Allowed<h1>")        
    else:
        user=emailBackend.authenticate(request, username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
          login(request,user)
          if user.user_type=="1":
           return HttpResponseRedirect('/admin_home')
          elif user.user_type=="2":
               return HttpResponse("Login Successful")
             #return HttpResponseRedirect(reverse("staff_home"))
          else:
               return HttpResponseRedirect(reverse("student_home"))            
        else:
          messages.error(request, "Wrong password. Please retry.")
          return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User: " +request.user.email+"User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")