from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPg, name='login'),
    path('signout/', views.signoutPg , name='signout'),
    path('api_users/', views.apiAllUsers , name='api_users'),
]
