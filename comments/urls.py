from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentListCreate.as_view()),
    path('<int:pk>/', CommentRetrieveUpdateDelete.as_view()),
]