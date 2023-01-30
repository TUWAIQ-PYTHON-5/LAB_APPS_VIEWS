from django.urls import path
from . import views


app_name = "AppAhmed"

urlpatterns=[
    path("",views.index ,name="home_page"),
    path("about/",views.index_about ,name="about")
]