from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', profiles, name='profiles'),
    path('user-profile/<str:pk>/', user_profile, name='user-profile'),
    path('account/', user_account, name='account'),
    path('update-account/', update_account, name='update-account'),
    path('create-skill/', create_skill, name='create-skill'),
    path('update-skill/<str:pk>/', update_skill, name='update-skill'),
    path('delete-skill/<str:pk>/', delete_skill, name='delete-skill'),
    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>/', view_message, name='message'),
]
