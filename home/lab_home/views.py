from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
 the_word="Hello World, This is my new HOME !"
 return HttpResponse(the_word)
def about(request):
 word2="A simple paragraph about the website."
 return HttpResponse(word2)