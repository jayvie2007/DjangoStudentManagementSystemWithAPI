from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import AccountModel
from .serializers import UserSerializer

from constant.status_code import * 

import uuid
# Create your views here.

class registerUser(APIView):
    def get(self, request):
        users = AccountModel.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response({"User Registered": serializers.data})
