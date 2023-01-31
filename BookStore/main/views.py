from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request : HttpRequest):

    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)

def about(request : HttpRequest):

    result = "It is a webpage during the course of learning Django"

    return HttpResponse(result)