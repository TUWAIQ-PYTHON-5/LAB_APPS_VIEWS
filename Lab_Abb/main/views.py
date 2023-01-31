from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request: HttpRequest):
    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)

def about(request: HttpRequest):
    
    result = "This is my first project."

    return HttpResponse(result)