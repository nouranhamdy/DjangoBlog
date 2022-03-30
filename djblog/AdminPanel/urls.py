from django.urls import path #,include
from Blog import views
from . import views as Adminviews
urlpatterns = [
    path('',Adminviews.AdminPanel , name='admin_panel'),
    path('login',views.loginPg , name='login'),
    path('signup',views.register , name='signup'),
    path('signout',views.signoutPg , name='signout'),
    path('AdminPanel',Adminviews.AdminPanel, name="Admin_Panel"),
    path('AdminPosts',Adminviews.adminPosts, name="Admin_posts"),
    path('post-add',Adminviews.addPost, name="post-add"),
    path('post-edit/<post_id>',Adminviews.editPost, name="post-edit"),
    path('post-del/<post_id>',Adminviews.postDel, name="post-delete"),

    path('admin_users',Adminviews.adminUsers , name='admin_users'),
    path('user-block/<user_id>',Adminviews.userBlock , name='user-block'),
    path('user-promote/<user_id>',Adminviews.userPromote , name='user-promote'),

    path('categ-page',Adminviews.adminCategories , name='categ-page'),
    path('categ-add',Adminviews.addCategory , name='categ-add'),
    path('categ-edit/<category_id>',Adminviews.editCategory , name='categ-edit'),
    path('categ-del/<category_id>',Adminviews.categoryDelete , name='categ-delete'),
]