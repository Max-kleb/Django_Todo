from django.urls import path
from .views import create_task, update_task, display_task, delete_task

urlpatterns = [
    path("api/tache", create_task, name='create_task'),
   # path("api/tache/<int:task_id>", update_task, name='update_task'),
    #path("api/tache/<int:list_id>", display_task, name='display_task'),
    path("api/tache/<int:task_id>", delete_task, name='delete_task'),
]

