from django.urls import path
from . import views

app_name = "first app"

urlpatterns = [
    path("", views.hello, name="hello"),
    path("about/", views.idea, name=" about the website")]