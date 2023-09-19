from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import UserRegistration
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer,UserLogin

class UserRegistrationAPI(APIView):
    permission_classes = [AllowAny]
    

    def get(self, request, user_id=None):
        if user_id:
            user = get_object_or_404(UserRegistration, pk=user_id)
            serializer = UserRegistrationSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        users = UserRegistration.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            user = UserRegistration.objects.get(id=user_id)
        except UserRegistration.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        try:
            user = UserRegistration.objects.get(id=user_id)
        except UserRegistration.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UserLoginAPI(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")
        
        user = UserRegistration.objects.filter(Q(email=email) & Q(password=password)).first()
        
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            response = {
                'detail': 'Login successful',
                'user_id': user.id,
                'access_token': access_token,
                'refresh_token': refresh_token,
                'status': status.HTTP_200_OK
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'detail': 'Invalid email / Password'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SendEmailAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        message = request.data.get('message')
        
        if email and message:
            # Send the email
            from_email = 'contact2tayib@gmail.com'
            recipient_list = [email]

            try:
                send_mail(
                    subject="Hello",
                    message=message,
                    from_email='contact2tayib@gmail.com',
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Email could not be sent.', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Both email and message fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

