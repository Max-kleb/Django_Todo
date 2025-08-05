from django.urls import path
from .views import signup, login, profile

urlpatterns = [
    path('auth/signup', signup, name='signup'),
    path('auth/login', login, name='login'),
    path('profile', profile, name='profile'),
]