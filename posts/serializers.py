from rest_framework import serializers

from comments.serializers import CommentSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('__all__')
    comments = CommentSerializer()

