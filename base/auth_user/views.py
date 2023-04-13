from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import AccountModel
from .serializers import UserSerializer

from constant.status_code import * 

import uuid
# Create your views here.

class getUser(APIView):
    def get(self,request):
        users = AccountModel.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response({"User Registered": serializers.data})

class registerUser(APIView):
    def post(self,request):
        #emailInput = request.data['email']
        #userInput = request.data['username']
        passwordInput = request.data['password']
        passwordInput2 = request.data['password2']

        serializers = UserSerializer(data=request.data)

        if passwordInput != passwordInput2:
            message = ("Password does not match!")
            return Response(data={"status":bad_request, "message": message})      

        uid = generate_uid()
        request.data._mutable=True
        request.data['uid'] = uid
        request.data._mutable=False
        
        if serializers.is_valid():
            #uncomment the serializers.save() if you want to save the data
            #serializers.save()
            message = ("You have successfully registered")
            return Response(data={"status": created, "message": message, "Users":serializers.data})
        return Response(serializers.errors, status=bad_request)

def generate_uid():
    uid = uuid.uuid4().hex[-8:]
    return uid