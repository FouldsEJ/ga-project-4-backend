from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()




class Like(models.Model):
    post_id = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
      return f"Post id: {self.post_id}"