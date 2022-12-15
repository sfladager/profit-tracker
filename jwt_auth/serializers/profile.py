from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# Serializer to be used for editing profile details
class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile_image')