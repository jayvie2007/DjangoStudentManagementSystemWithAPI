from .models import AccountModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'
        
class UserSerialiazerEditAPI(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['fname', 'lname']

class Login_UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = False)
    email = serializers.CharField(required = False)
    password = serializers.CharField(required = False)
    class Meta:
        model = AccountModel
        fields = ['username', 'email', 'password' ]
