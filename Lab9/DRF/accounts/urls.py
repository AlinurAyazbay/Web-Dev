# api/urls.py

from django.urls import path
from .views import RegisterView, LoginView, get_authenticated_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', get_authenticated_user, name='get_user'),
]