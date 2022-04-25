from rest_framework import serializers

from comments.serializers import CommentSerializer, PopulatedCommentSerializer
from jwt_auth.serializers import MinimalUserSerializer
from likes.serializers import LikeSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
  created_datetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
  class Meta:
    model = Post
    fields = ('__all__')
    comments = CommentSerializer

class PopulatedPostSerializer(PostSerializer):
  # comments = PopulatedCommentSerializer(many=True)
  # likes = LikeSerializer(many=True)
  created_by = MinimalUserSerializer()

