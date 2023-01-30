from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse
 
def index(request:HttpRequest):
 result=" Hello World, This is my new HOME !"
 return HttpResponse(result)

def index1(request:HttpRequest):
 result=" A simple paragraph about the website."
 return HttpResponse(result)
