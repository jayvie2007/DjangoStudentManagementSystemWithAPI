from django.shortcuts import render
from .models import AccountModel

import uuid

def index(request):
    return render(request, 'auth_user/index.html')

def register(request):
    return render(request, 'auth_user/register.html')

def login(request):
    return render(request, 'auth_user/login.html')