from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

from .serializers.common import UserSerializer
from .serializers.populated import PopulatedUserSerializer

# modules
from datetime import datetime, timedelta
import jwt

#import settings module
from django.conf import settings # we can get the SECRET_KEY from here


User = get_user_model()
# Endpoint: register/
class RegisterView(APIView):

  def post(self, request):
    try:
      #1 Take user data and validate it 
      user_to_register = UserSerializer(data=request.data)
      if user_to_register.is_valid():
        user_to_register.save()
        return Response('Registration Successful', status.HTTP_201_CREATED)
      return Response(user_to_register.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
      print(e)
      return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']
    # Query user email in database
    try:
      user_to_login = User.objects.get(email=email)
    except User.DoesNotExist as e:
      print(e) 
      raise PermissionDenied('Invalid Username or Password')

    if not user_to_login.check_password(password):
      print('Password is incorrect')
      raise PermissionDenied('Invalid Username or Password')

    # Need to build a date 7 days in the future to give expitation time for token
    dt = datetime.now() + timedelta(days=7)
    dt_as_seconds = int(dt.strftime('%s'))
    token = jwt.encode(
      {'sub': user_to_login.id, 'exp': dt_as_seconds },
      settings.SECRET_KEY,
      'HS256'
    )
    print(token)
    return Response({
      'token': token,
      'message': f'Welcome back, {user_to_login.username}'
    }, status.HTTP_202_ACCEPTED)

class ProfileView(APIView):
  
  def get(self, _request, pk):
    print("REQUEST USER ->", pk)
    profile_to_get = User.objects.get(pk=pk)
    serialized_profile = PopulatedUserSerializer(profile_to_get)
    print("REQUEST REQUEST ->", serialized_profile.data)
    return Response(serialized_profile.data)