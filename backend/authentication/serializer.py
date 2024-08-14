from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" #serializing all fields
        # fields = ['password', 'email'] #serializing all fields
        