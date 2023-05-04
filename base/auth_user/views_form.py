from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UserData
from .forms import UserForm

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
                    password = make_password(password),
                )
                new_user.save()
                
                return redirect('login_user',{
                    'form': UserForm(),
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


def generate_uid2():
    uid = random.randint(10000000, 99999999)
    return uid

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']

        User = get_user_model()
        user1 = User.objects.all()
        user = auth.authenticate(request, username=username_or_email, password=password)
        print(user1)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')

        # try:
        #             if '@' in username_or_email:
        #                 email = CustomUser.objects.get(email = username_or_email) 
        #                 if user is not None:
        #                     auth.login(request,user)
        #                     return redirect('index')
        #                 else:
        #                     messages.info(request, 'Invalid Username or Password')
        #                     return redirect('login_user')
        #             else: 
        #                 input_user = CustomUser.objects.get(username = username_or_email)
        #                 if user is not None:
        #                     auth.login(request,user)
        #                     return redirect('index')
        #                 else:
        #                     messages.info(request, 'Invalid Username or Password')
        #                     return redirect('login_user')
        # except:
        #     return render(request, "auth_user/login.html")
        
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
def edit(request):
    return render(request, 'auth_user/edit.html')