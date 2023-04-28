from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from .models import CustomUser

import uuid


import uuid

def index(request):
    return render(request, 'auth_user/index.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        uid = generate_uid()

        if password == confirm_password:
            if CustomUser.objects.filter(username=username):
                messages.info(request, 'Username already exist!')
                return redirect('register_user')
            if CustomUser.objects.filter(email=email):
                messages.info(request, 'Email already exist!')
                return redirect('register_user')
            else:
                new_user = CustomUser.objects.create(
                    uid = uid,
                    first_name = first_name,
                    middle_name = middle_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password,
                )
                new_user.save()
                
                return redirect('login_user',{
                    'success': True,
                })
        else:
            messages.info(request, 'Password does not match')
            print("error")
            return redirect('register_user')
    return render(request, 'auth_user/register.html')

def generate_uid():
    uid = uuid.uuid4().hex[-8:]
    return uid

def login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        user = auth.authenticate(request, username=username_or_email, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        print("invalid")
        return render(request, "auth_user/login.html")
    
def logout(request):
    auth.logout(request)
    return redirect('index')
        