from django.urls import path
from foodaapp import views


urlpatterns = [
    path("", views.home, name="home"),
    path("barranco", views.barranco, name="barranco")
]