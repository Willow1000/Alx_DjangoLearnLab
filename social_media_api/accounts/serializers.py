from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
# token = Token.objects.create(user = get_user_model().objects.create_user)
class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    class Meta:
        model = User
        fields = "__all__"

  