from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings

class UserRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def str(self):
        return self.email

class UserLogin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def str(self):
        return self.email
    
class SendEmail(models.Model):
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.email