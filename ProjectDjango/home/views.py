from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest , HttpResponse

def new_home(request: HttpRequest):
    result = "Hello World, This is my new HOME !"
    return HttpResponse(result)




def new_mine(request: HttpRequest):
    result = "A simple project with all the content!"
    return HttpResponse(result)

