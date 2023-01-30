from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def hello(request : HttpRequest):

    phrase = "Hello World, This is my new HOME !"
    return HttpResponse(phrase)

def idea(request : HttpRequest):

    phrase="Our website will help you learn python language ."
    return HttpResponse(phrase)