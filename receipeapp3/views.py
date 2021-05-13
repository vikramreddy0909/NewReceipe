from django.shortcuts import render
from .models import Receipe
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def login_user(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')

def save_details(request):
    User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
    return HttpResponseRedirect('/receipeapp3/register/')

def login_sucess_or_not(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/receipeapp3/items/')
    else:
        return HttpResponse("<html><body bgcolor='red'><h1>'Invalid username Or Password '</h1></body></html>")


def items(request):
    receipes=Receipe.objects.all()
    return render(request,'items.html',{'receipe':receipes})

def details(request,receipe_id):
    receipes1=Receipe.objects.get(id=receipe_id)
    return render(request,'details.html',{'receipe1':receipes1})

def create_page(request):
    return render(request,'create_page.html')

def save_receipe(request):
    Receipe.objects.create(name=request.POST['name'],process=request.POST['process'],ingridients=request.POST['ingridients'],pub_date=timezone.now(),image=request.FILES['image'])
    return HttpResponseRedirect('/receipeapp3/items/')

def delete_receipe(request,receipe_id):
    Receipe.objects.get(pk=receipe_id).delete()
    return HttpResponseRedirect('/receipeapp3/items/')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/receipeapp3/')
