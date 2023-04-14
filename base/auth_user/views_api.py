from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AccountModel
from .serializers import UserSerializer, UserSerialiazerEditAPI, Login_UserSerializer

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
        errors = {}

#initialize the data from the database
        required_fields = ['fname','lname','email','username','password','password2']
#then loop the data if that specific field is in the request.data if not error will be returned
        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error
            if len(errors) != 0:
                return Response(data={"status": bad_request , 'message':errors}, status=bad_request)
        
        emailInput = request.data['email']
        userInput = request.data['username']
        passwordInput = request.data['password']
        passwordInput2 = request.data['password2']
       
        if 'email' in request.data and AccountModel.objects.filter(email = emailInput).count() != 0:
            errors['email']=(f"the email {emailInput} is already taken!")
        if 'username' in request.data and AccountModel.objects.filter(username = userInput).count() != 0:
            errors['username']=(f"the username {userInput} is already taken!")
        if passwordInput != passwordInput2:
            errors['password']=(f"the password does not match")
        if len(errors) != 0:
            return Response(data={'message':errors}, status=bad_request)
             
        uid = generate_uid()
        request.data._mutable=True
        request.data['uid'] = uid
        request.data._mutable=False
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={"status": created, "message": register_success, "Users":serializers.data})
        return Response(serializers.errors, status=bad_request)

class editUser(APIView):
    def put(self, request, uid):
        errors = {}
        
        required_fields = ['fname','lname']

        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error
            if len(errors) != 0:
                return Response(data={'message':errors,}, status=bad_request)

        try:
            users = AccountModel.objects.get(uid = uid)
        except AccountModel.DoesNotExist:
            return Response(data={'status': not_found})
        
        serializers = UserSerialiazerEditAPI(users, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={'status':ok, 'message':updated})
        return Response(serializers.errors, status=bad_request)
        
class deleteUser(APIView):
    def delete(self, request, uid):
        try:
            users = AccountModel.objects.get(uid = uid)
        except AccountModel.DoesNotExist:
            return Response(data={'status': not_found})
        users.delete()
        return Response(data={'status': no_content})
    

class loginAPI(APIView):
    def post(self, request):
        errors = {}

        required_fields = ['username', 'password', 'email']

        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error

        if len(errors)!=0:
            return Response(data={'message':errors,}, status=bad_request)
        
        userInput = request.data['username']
        emailInput = request.data['email']
        passwordInput = request.data['password']
        serializers = Login_UserSerializer(data = request.data)
        if serializers.is_valid():
            try:
                user = AccountModel.objects.get(username = userInput)
            except AccountModel.DoesNotExist:

                try:
                    email = AccountModel.objects.get(email = emailInput)
                except:
                    return Response(data={"status": bad_request, 'message': incorrect_value})
                
        if user.password == passwordInput:     
            return Response(data={"status": ok, 'message': login_success})
        return Response(data={"status": bad_request, 'message': incorrect_value})



def generate_uid():
    uid = uuid.uuid4().hex[-8:]
    return uid