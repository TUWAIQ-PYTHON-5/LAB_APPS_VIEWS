
from django.urls import path
import views
app_name="main"
urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.index1,name='index1'),
]