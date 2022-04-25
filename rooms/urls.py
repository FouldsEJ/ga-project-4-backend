from django.urls import path
from .views import *

urlpatterns = [
    path('', RoomListCreate.as_view()),
    path('<int:pk>/', RoomRetrieveUpdateDestroy.as_view())
]