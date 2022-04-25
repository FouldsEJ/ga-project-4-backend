from django.urls import path 
from .views import CredentialsView, RegisterView, LoginView, AllCredentialsView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('allusers/', AllCredentialsView.as_view()),

]