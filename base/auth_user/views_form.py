from django.shortcuts import render
from .models import AccountModel

import uuid

def index(request):
    return render(request, 'auth_user/index.html')