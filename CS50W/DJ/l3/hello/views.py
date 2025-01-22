from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. something thet user might want to see

def index(request):
    return render(request, "hello/index.html")

def elias(request):
    return HttpResponse("Hello Coumine")

def ronaldo(request):
    return HttpResponse("sui")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()} !")



