from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenVerifyView
from .views import UserRegistrationAPI, UserLoginAPI ,SendEmailAPI

urlpatterns = [
    path('api/register/', UserRegistrationAPI.as_view(), name='register'),
    path('api/register/<int:user_id>/', UserRegistrationAPI.as_view(), name='register_user_api_detail'),
    path('api/login/', UserLoginAPI.as_view(), name='login'),
    path('api/send_email/', SendEmailAPI.as_view(), name='send_email'),
]