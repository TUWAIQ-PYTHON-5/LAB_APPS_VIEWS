from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def index(request : HttpRequest):
    msg="welcome to yourHome Page"
    return HttpResponse(msg)