from django.urls import path
from . import views
app_name="first_app"

urlpatterns = [
path("path/", views.my_word, name="path")
]