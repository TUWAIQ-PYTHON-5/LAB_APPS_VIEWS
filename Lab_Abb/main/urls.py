from django.urls import path
from . import views


appname = "main"

urlpatterns= [
    path("", views.home, name = "home_page"),
    path("about/", views.about, name = "about_page")

]