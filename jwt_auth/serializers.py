from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from rooms.serializers import RoomSerializer
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation', 'date_joined', 'first_name', 'last_name', 'image', 'description', 'ability', 'gender', 'town', 'country', 'rooms')


class PopulatedUserSerializer(UserSerializer):
  rooms = RoomSerializer(many=True)

class MinimalUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'image', 'password', 'password_confirmation', 'date_joined', 'ability')



# class UserShowSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('__all__')