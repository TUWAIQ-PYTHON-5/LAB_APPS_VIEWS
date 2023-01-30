from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def word(request):
    return HttpResponse("Hello World, This is my new HOME !")

def my_word(request):
    return HttpResponse("this call for complete")


