from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("about/", views.about, name="about_page"),
]