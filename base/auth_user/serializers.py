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