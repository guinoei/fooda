from django.shortcuts import render
from .models import Restaurant


def home(request):
    return render(request, 'home.html', {})


def barranco(request):
    barranco = Restaurant.objects.all()
    return render(request, 'barranco.html', {'barranco':barranco})