from django.urls import path
from .views import create_list, display_list, update_list, delete_list


urlpatterns = [
    path('POST/api/liste', create_list ),
    path('GET/api/liste', display_list ),
    path('PUT/api/liste', update_list ),
    path('DELETE/api/liste', delete_list ),
]