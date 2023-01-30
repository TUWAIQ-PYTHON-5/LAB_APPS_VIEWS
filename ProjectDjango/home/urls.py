from django.urls import path

from . import views


app_name = "home"

urlpatterns = [

     path("", views.new_home, name="new_home"),
     path("Home/", views.new_mine, name="new_mine"),
]

