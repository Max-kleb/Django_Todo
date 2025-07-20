from django.urls import path
from .views import router


urlpatterns = [
    path('/api/liste', router ),
]