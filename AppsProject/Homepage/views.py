from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def get_homepage(request : HttpRequest) :

    content = "Hello World, This is my new HOME !"

    return HttpResponse(content)

def get_about(request : HttpRequest) :

    content = "I made this website to test my knowledge about Django apps "

    return HttpResponse(content) 