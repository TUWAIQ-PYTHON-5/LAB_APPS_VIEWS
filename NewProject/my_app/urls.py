from django.urls import path
from . import views 


app_name = "my_app"

urlpatterns = [
    path("home/", views.index, name="home_page"),
    path("about/" , views.aboutfunction, name="about_page")
]
