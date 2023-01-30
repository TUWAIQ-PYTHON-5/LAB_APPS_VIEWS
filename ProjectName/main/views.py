from django.shortcuts import render

# Create your views here.


from django.http import HttpRequest , HttpResponse


def home(request: HttpRequest):
    result = "Hello World, This is my new HOME !"
    return HttpResponse(result)


def about (requset : HttpRequest):
    result ="This is a test program."
    return HttpResponse (result)


