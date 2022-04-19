from django.urls import path
from .views import *

urlpatterns = [
    path('', LikeListCreate.as_view()),
    # path('<int:pk>/', LikeRetrieveUpdateDelete.as_view()),
]