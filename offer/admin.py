from django.contrib import admin
from .models import UserRegistration,UserLogin,SendEmail

@admin.register(UserRegistration)
class UserRegister(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(UserLogin)
class UserLogin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(SendEmail)
class SendEmail(admin.ModelAdmin):
    list_display = ['email','message']