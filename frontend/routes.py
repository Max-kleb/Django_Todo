from django.urls import path
from .views import home, login, signup
urlpatterns = [
    path("", home),
    path("login", login),
    path("signup", signup)
]
