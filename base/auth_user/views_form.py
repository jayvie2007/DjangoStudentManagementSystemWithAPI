from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AccountModel


import uuid

def index(request):
    return render(request, 'auth_user/index.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.info(request, 'Username already exist!')
                return redirect('register')
            if User.objects.filter(email=email):
                messages.info(request, 'Email already exist!')
                return redirect('register')
            else:
                new_user = User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                )
                new_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('login')
    return render(request, 'auth_user/register.html')

def login(request):

    return render(request, 'auth_user/login.html')