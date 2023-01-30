from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.



def home(request: HttpRequest):
    
    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)


def about (requset : HttpRequest):
    result ="Welcome, this is a test program to test my understanding of the previous lesson. Thanks"

    return HttpResponse (result)
