from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
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
