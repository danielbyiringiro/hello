from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"lecture3/index.html")

def daniel(request):
    return HttpResponse("Hello, Daniel!")

def greet(request, name):
    return render(request, "lecture3/greet.html",{
        "name": name.capitalize()
    })