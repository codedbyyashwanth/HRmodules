from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
import jwt
from django.conf import settings

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")
        if len(auth_token) != 2:
            return None

        token = auth_token[1]

        try:
            payload = jwt.decode(token, str(settings.JWT_SECRET_KEY), algorithms=["HS256"])
            username = payload['user_name']  # Correct the payload key
            user = User.objects.get(username=username)  # Correct the user model and field
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token is expired, login again')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Token is invalid')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return None