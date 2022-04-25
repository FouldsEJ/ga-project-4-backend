from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Room (models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=200, blank=True)
  users = models.ManyToManyField(User, related_name='rooms')
  created_datetime = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.name