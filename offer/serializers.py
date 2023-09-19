from rest_framework import serializers
from .models import UserRegistration, UserLogin, SendEmail

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['id', 'username', 'password', 'email']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id', 'email', 'password', 'access_token', 'refresh_token']

class SendEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendEmail
        fields = ['email','message']