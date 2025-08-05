from django.urls import path
from .views import ListView

urlpatterns = [
    path('api/liste', ListView.as_view()),
    path('api/liste/<int:list_id>', ListView.as_view()),
]