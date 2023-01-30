from django.shortcuts import render
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def index(request : HttpRequest):

    result =  "Hello World, This is my new HOME !"


    return HttpResponse(result)

def about(request : HttpRequest):

    result =  "A website for the purpose of training and presenting some solutions to the customer"


    return HttpResponse(result)
