from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
from myapp.forms import *
from django.contrib.auth import authenticate, login, logout



def base(req):
    return render(req,'base.html')

def home(req):
    return render(req,'home.html')

def registerpage(req):
    form= customform()
    if req.method=='POST':
        username=req.POST.get('username')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            user=Custom_user.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=confirm_password)
            return redirect('loginpage')

    return render(req,'registerpage.html' ,{'form':form})

def loginpage(req):
    form= loginform()
    if req.method=='POST':
        
        username=req.POST.get("username")
        password=req.POST.get("password")
        
        user=authenticate(username=username,password=password)
        
        if user:
            login(req,user)
            
            return redirect("home")
    return render(req,'loginpage.html' ,{'form':form})
