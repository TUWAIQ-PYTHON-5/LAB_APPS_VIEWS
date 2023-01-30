from django.urls import path
from . import views

app_name = "Homepage"

urlpatterns = [
    path("", views.get_homepage, name = "Homepage"),
    path("about/", views.get_about, name = "about")
]