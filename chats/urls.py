
from django.urls import path
from .views import *


urlpatterns = [
    path('', ChatListCreate.as_view()),
    path('<int:pk>/', ChatUpdateDestroy.as_view()),
    path('<int:pk>/detail', ChatDetail.as_view()),
]