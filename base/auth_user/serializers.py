from .models import CustomUser, UserData
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('id', 'last_login','is_superuser','is_staff','is_active','date_joined','groups','user_permissions')
        
class UserSerialiazerEditAPI(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name' ,'last_name']

class Login_UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = False)
    email = serializers.CharField(required = False)
    password = serializers.CharField(required = False)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password' ]

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ('id', 'student_number')

class Students_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ('id',)