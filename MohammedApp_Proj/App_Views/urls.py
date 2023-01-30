from django.urls import path
from . import views


app_name = "App_Views"

urlpatterns = [
    path("home_page/", views.welcome, name="home_page"),
    path('',views.welcome_1, name= "about")
]
