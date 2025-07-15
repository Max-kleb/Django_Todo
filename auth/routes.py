from django.urls import path
from .views import signup

urlpaterns = [
    path('auth/sign', signup, name='signup' ),
]