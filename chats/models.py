from django.db import models
from django.contrib.auth import get_user_model
from rooms.models import Room

User = get_user_model()

# Create your models here.

class Chat(models.Model):
  text = models.CharField(max_length=1500)
  created_datetime = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, related_name='chats', on_delete=models.CASCADE)

  def __str__(self):
    return self.text
