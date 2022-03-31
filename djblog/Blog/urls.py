from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('home/', HomeView.as_view(), name='home'),
    path('',views.PostView, name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.loginPg, name='login'),
    path('logout/', views.signoutPg , name='logout'),
    path('api_users/', views.apiAllUsers , name='api_users'),
    path('article/<post_id>',views.ArticleDetailView, name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<cats>/',views.CategoryView, name="category"),
    path('category-list/',views.CategoryListView, name="category-list"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


