from django.db import models

# Create your models here.
class Post (models.Model):
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=1500)
  creation_datetime = models.DateTimeField(null=True)
  image_url = models.CharField(max_length=200, blank=True)
  video_url = models.CharField(max_length=200, blank=True)
  # created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

  def __str__(self):
    return self.title