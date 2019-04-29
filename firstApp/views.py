from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginCred
# Create your views here.

def index(request):
    #return HttpResponse('hello world')
    return render(request, 'firstApp/index.html')



def about(request):
    #return HttpResponse('hello world')
    return render(request, 'firstApp/about.html')


def coolwebsites(request):
    #return HttpResponse('hello world')

    
    data = {}
    data["data"] = []
    data["data"].append(['Google',"google.com"])
    data["data"].append(['Minecraft',"minecraft.net"])
    data["data"].append(["Amazon","amazon.net"])
    
    return render(request, 'firstApp/coolwebsites.html', data)


def form(request):
    #return HttpResponse('hello world')
    login = LoginCred.objects.all()
    data_dict = {}
    data_dict["logins"] = login
    return render(request, 'firstApp/form.html', data_dict)
    

def greet(request):
    #return HttpResponse('hello world')
    user_name = request.POST.get('user')
    pass_ = request.POST.get('pass')
    login = LoginCred.objects.all()
    data = {}
    data["user"] = user_name
    data["pass"] = pass_
    data["logins"] = login
    

    return render(request, 'firstApp/greet.html', data)
    


def register(request):
    #return HttpResponse('hello world')
    login = LoginCred.objects.all()
    data_dict = {}
    data_dict["logins"] = login
    return render(request, 'firstApp/register.html', data_dict)
    