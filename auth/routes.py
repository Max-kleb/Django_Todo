from django.urls import path
from .views import signup, login

urlpaterns = [
    path('auth/sign', signup, name='signup' ),
    path('auth/login', login , name='login'),
]