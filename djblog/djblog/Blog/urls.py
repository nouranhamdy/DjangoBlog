from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from . import views

urlpatterns = [
    #path('home/', HomeView.as_view(), name='home'),
    path('',HomeView.as_view(), name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.loginPg, name='login'),
    path('logout/', views.signoutPg , name='logout'),
    path('api_users/', views.apiAllUsers , name='api_users'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/',CategoryView, name="category"),
]

