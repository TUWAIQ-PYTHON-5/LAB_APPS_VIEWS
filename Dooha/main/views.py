from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def home (request : HttpRequest):
    
    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)

def about (request : HttpRequest):
    
    result = "this is my first page !"

    return HttpResponse(result)
