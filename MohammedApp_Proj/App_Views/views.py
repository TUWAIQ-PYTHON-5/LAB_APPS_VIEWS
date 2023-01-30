from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def welcome(request: HttpRequest):

    result = "Hello World, This is my new HOME !"

    return HttpResponse(result)


def welcome_1(requset: HttpRequest):

    result = "A simple paragraph about the website"

    return HttpResponse(result)

