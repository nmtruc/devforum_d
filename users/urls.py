from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', profiles, name='profiles'),
    path('user-profile/<str:pk>/', user_profile, name='user-profile'),
]
