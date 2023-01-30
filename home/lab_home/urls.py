from . import views
from django.urls import path
app_name = "lab_home"

urlpatterns = [
    path("home/", views.home, name="path"),
    path("about/",views.about, name="path")
]