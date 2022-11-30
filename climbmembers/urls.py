from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.register_user, name='register-user'),
    path('login_user', views.login_user, name='login-user'),
    path('logout', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'), 
    
]