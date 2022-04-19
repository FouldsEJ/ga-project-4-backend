from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'text', 'image_url', 'video_url')

# Register your models here.
admin.site.register(Post, PostAdmin)