from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request : HttpRequest):

    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)

def about(request : HttpRequest):

    content = "In this web site you will find my daily blogs. Hope you enjoy."
    return HttpResponse(content)
