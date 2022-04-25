

from rest_framework import serializers

from jwt_auth.serializers import MinimalUserSerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('__all__')


class PopulatedCommentSerializer(CommentSerializer):
  created_by = MinimalUserSerializer()


