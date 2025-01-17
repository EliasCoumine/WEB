from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. something thet user might want to see

def index(request):
    return HttpResponse("Hello world")



