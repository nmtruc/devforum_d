from django.urls import path
from .views import *


urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project', create_project, name='create-project'),
    path('update-project/<str:pk>/', update_project, name='update-project'),
    path('delete-project/<str:pk>/', delete_project, name='delete-project'),
]
