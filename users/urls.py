from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', profiles, name='profiles'),
    path('user-profile/<str:pk>/', user_profile, name='user-profile'),
    path('account/', user_account, name='account'),

]
