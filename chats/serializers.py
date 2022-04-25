
from rest_framework import serializers

from jwt_auth.serializers import UserSerializer
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chat
    fields = ('__all__')


class PopulatedChatSerializer(ChatSerializer):
  created_by = UserSerializer()