from django.urls import path
from . import views


app_name = "AppAhmed"

urlpatterns=[
    path("home_page/",views.index ,name="home_page")
]