from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Comment(models.Model):
  text = models.TextField(max_length=300)
  created_datetime = models.DateTimeField(auto_now_add=True)
  updated_datetime = models.DateTimeField(auto_now=True)
  post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

  def __str__(self):
    return self.text

