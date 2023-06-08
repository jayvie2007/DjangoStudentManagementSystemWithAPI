from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import CustomUser, UserData
from .serializers import UserSerializer, UserSerialiazerEditAPI, Login_UserSerializer, Student_Serializer, Students_Serializer

from constant.status_code import * 

import random

import uuid

def generate_uid():
    uid = uuid.uuid4().hex[-8:]
    return uid

def generate_uid2():
    uid = random.randint(10000000, 99999999)
    return uid

class StatusPageViewUserAPI(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def get_user(self,request):
        users = CustomUser.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response({"User Registered": serializers.data})
    
    @action(detail=False, methods=['POST'])
    def create_user(self,request):
        errors = {}

    #initialize the data from the database
        required_fields = ['first_name','middle_name' ,'last_name','email','username','password','password2']
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
        
        if 'email' in request.data and CustomUser.objects.filter(email = emailInput).count() != 0:
            errors['email']=(f"the email {emailInput} is already taken!")
        if 'username' in request.data and CustomUser.objects.filter(username = userInput).count() != 0:
            errors['username']=(f"the username {userInput} is already taken!")
        if passwordInput != passwordInput2:
            errors['password']=(f"the password does not match")
        if len(errors) != 0:
            print(make_password("password"))
            return Response(data={'message':errors}, status=bad_request)

        passwordInput=make_password(passwordInput)
        uid = generate_uid()
        request.data._mutable=True
        request.data['uid'] = uid
        request.data['password'] = passwordInput
        request.data._mutable=False
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={"status": created, "message": register_success, "Users":serializers.data})
        return Response(serializers.errors, status=bad_request)
    
    @action(detail=False, methods=['PUT'])
    def edit_user(self, request, uid):
        errors = {}
        
        required_fields = ['first_name','middle_name','last_name']

        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error
            if len(errors) != 0:
                return Response(data={'message':errors,}, status=bad_request)

        try:
            users = CustomUser.objects.get(uid = uid)
        except CustomUser.DoesNotExist:
            return Response(data={'status': not_found})
        
        serializers = UserSerialiazerEditAPI(users, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={'status':ok, 'message':updated})
        return Response(serializers.errors, status=bad_request)
    
    @action(detail=False, methods=['DELETE'])
    def delete_user(self, request, uid):
        try:
            users = CustomUser.objects.get(uid = uid)
        except CustomUser.DoesNotExist:
            return Response(data={'status': not_found, 'message': does_not_exist})
        users.delete()
        return Response(data={'status': no_content, 'message':"Deleted Successfully"})
    
class StatusPageViewStudentAPI(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def get_student(self,request):
        student = UserData.objects.all()
        serializers = Students_Serializer(student, many=True)
        return Response({"Student Registered": serializers.data}) 
    
    @action(detail=False, methods=['POST'])
    def create_student(self,request):
        errors = {}

    #initialize the data from the database
        required_fields = ['first_name','middle_name' ,'last_name','gender','year','course','semester']
    #then loop the data if that specific field is in the request.data if not error will be returned
        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error
            if len(errors) != 0:
                return Response(data={"status": bad_request , 'message':errors}, status=bad_request)
        
        first_input = request.data['first_name']
        middle_input = request.data['middle_name']
        last_input = request.data['last_name']
        
        if 'first_name' in request.data and UserData.objects.filter(first_name = first_input).count() != 0 and 'middle_name' in request.data and UserData.objects.filter(middle_name = middle_input).count() != 0 and 'last_name' in request.data and UserData.objects.filter(last_name = last_input).count() != 0:
            errors['name']=(f"the name {first_input} {middle_input} {last_input} is already in the list!")
        if len(errors) != 0:
            return Response(data={'message':errors}, status=bad_request)

        uid = generate_uid2()
        request.data._mutable=True
        request.data['student_number'] = uid
        request.data._mutable=False

        serializers = Students_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={"status": created, "message": register_success, "Users":serializers.data})
        return Response(serializers.errors, status=bad_request)
    
    @action(detail=False, methods=['PUT'])
    def edit_student(self, request, student_number):
        errors = {}
        
        required_fields = ['first_name','middle_name' ,'last_name','gender','year','course','semester']

        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error
            if len(errors) != 0:
                return Response(data={'message':errors,}, status=bad_request)

        try:
            users = UserData.objects.get(student_number = student_number)
        except UserData.DoesNotExist:
            return Response(data={'status': not_found})
        
        serializers = Student_Serializer(users, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data={'status':ok, 'message':updated})
        return Response(serializers.errors, status=bad_request)
    
    @action(detail=False, methods=['DELETE'])
    def delete_student(self, request, student_number):
        try:
            users = UserData.objects.get(student_number = student_number)
        except UserData.DoesNotExist:
            return Response(data={'status': not_found, 'message': does_not_exist})
        users.delete()
        return Response(data={'status': no_content, 'message':"Deleted Successfully"})

class StatusPageViewLoginUserAPI(viewsets.ViewSet):
    @action(detail=False, methods=['POST'])
    def login(self, request):
        errors = {}
        field_required_error = 'This field is required.'
        incorrect_value = 'Incorrect username or password.'
        ok = 'OK'
        login_success = 'Login successful.'
        bad_request = status.HTTP_400_BAD_REQUEST

        required_fields = ['username', 'password']

        for required_field in required_fields:
            if required_field not in request.data:
                errors[required_field] = field_required_error

        if len(errors) != 0:
            return Response(data={'message': errors}, status=bad_request)

        username_input = request.data['username']
        password_input = request.data['password']
        try:
            user = CustomUser.objects.get(username=username_input)
        except CustomUser.DoesNotExist:
            return Response(data={"status": bad_request, 'message': incorrect_value})

        if check_password(password_input, user.password):
            return Response(data={"status": ok, 'message': login_success})
        else:
            return Response(data={"status": bad_request, 'message': incorrect_value})
