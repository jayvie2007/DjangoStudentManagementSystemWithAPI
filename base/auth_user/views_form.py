from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserData
from .forms import UserForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

import random
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
                print("username already exist")
                message = 'Username already exist!'
                return render(request, 'auth_user/register.html', {
                    'register_error': True,
                    'messagestxt': message,
                })
            if CustomUser.objects.filter(email=email):
                print("email already exist")
                message = 'Email already exist!'
                return render(request, 'auth_user/register.html', {
                    'register_error': True,
                    'messagestxt': message,
                })
                   
            else:
                new_user = CustomUser.objects.create(
                    uid = uid,
                    first_name = first_name,
                    middle_name = middle_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = make_password(password),
                )
                #new_user.save()
                print("success")
                return render(request, 'auth_user/login.html',{
                    'form': UserForm(),
                    'success': True,
                })
        else:
            form = UserForm()
            messages.info(request, 'Password does not match')
            return redirect('auth_user/register.html', {
            'form': UserForm()
             })
        
    return render(request, 'auth_user/register.html')

def generate_uid():
    uid = uuid.uuid4().hex[-8:]
    return uid


def generate_uid2():
    uid = random.randint(10000000, 99999999)
    return uid

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username_or_email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, "auth_user/login.html")
    
def logout_view(request):
    auth.logout(request)
    return redirect('index')

# use @login_required to require authentication before accessing new page        
@login_required        
def database(request):
    return render(request, 'auth_user/database.html',{
        'userdatas': UserData.objects.all()
        })

@login_required     
def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_student_number = generate_uid2()
            new_first_name = form.cleaned_data['fname']
            new_middle_name = form.cleaned_data['mname']
            new_last_name = form.cleaned_data['lname']
            new_year = form.cleaned_data['year']
            new_course = form.cleaned_data['course']
            new_semester = form.cleaned_data['semester']

            new_user = UserData(
                student_number = new_student_number,
                fname = new_first_name,
                mname = new_middle_name,
                lname = new_last_name,
                year = new_year,
                course = new_course,
                semester = new_semester,
            ) 
            new_user.save()
            return render(request, 'auth_user/add.html', {
                'form': UserForm(),
                'success':True, 
            })
    else:
        form = UserForm()
    return render(request, 'auth_user/add.html',{
    'form': UserForm()
    })

@login_required     
def edit(request, student_number):
    if request.method =='POST':
        users = UserData.objects.get(student_number=student_number)
        form = UserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return render(request, 'auth_user/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        users = UserData.objects.get(student_number=student_number)
        form = UserForm(instance=users)
        return render(request, 'auth_user/edit.html', {
            'form':form
        })
    
@login_required 
def delete(request, student_number):
    if request.method =='POST':
        users = UserData.objects.get(student_number=student_number)
        users.delete()
        return HttpResponseRedirect(reverse('index'))