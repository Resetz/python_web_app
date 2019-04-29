from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('hello world')
    return render(request, 'index.html')

def about(request):
    #return HttpResponse('hello world')
    return render(request, 'about.html')

def oasis(request):
    #return HttpResponse('hello world')
    dataDictionary= {}
    dataDictionary["name"] = 'oasis'
    dataDictionary["name2"] = 'oasis2'
    dataDictionary["name3"] = 'oasis3'
    dataDictionary["name"] = True
    dataDictionary["range"] = range(1,6)
    dataDictionary["classtuff"] = [["Zak",19,"Mr.Zak", 90,89,0],["Challenges",18,"Mr.Zak", 87,83,3]]
    return render(request, 'oasis.html', dataDictionary)