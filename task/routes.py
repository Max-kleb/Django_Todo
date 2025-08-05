from django.urls import path
from .views import TaskView

urlpatterns = [
    path('api/task', TaskView.as_view()),
    path('api/task/<int:task_id>', TaskView.as_view()),
]
