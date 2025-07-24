from django.urls import path
from .views import create_list, display_list, delete_list , update_list


urlpatterns = [
    path('api/liste', create_list , name='create_list'),
    path('api/liste/<int:list_id>', update_list, name='update_list' ),
    path('api/liste/<int:user_id>', display_list , name='display_list'),
    path('api/liste/<int:list_id>', delete_list , name='delete_list'),   
]