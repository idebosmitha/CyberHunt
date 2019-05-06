from django.shortcuts import render


def home(request):
    return render(request, 'teams/home.html')


def login(request):
    return render(request, 'teams/login.html')


def register(request):
    return render(request, 'teams/register.html')
