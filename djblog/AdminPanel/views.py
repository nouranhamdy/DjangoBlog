
from django.shortcuts import render
from Blog.models import  Post , user , Category
from Blog.forms import PostForm , CategoryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import DetailView

# from AdminPanel.forms import PostForm

# Create your views here.
# admin CRUD
@login_required(login_url='login')
def AdminPanel(request):
    if request.user.is_superuser:
        return render(request,'admin/admin_panel.html')

def adminPosts(request): 
    posts = Post.objects.all()
    context = { "object_list" : posts}
    return render(request,'admin/posts.html', context)

def addPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('Admin_posts')
    post_form = PostForm()
    context = {'form': post_form}
    return render(request, 'admin/add_post.html', context)

def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form = PostForm(instance=post)

    if request.method =='POST':
        post_form = PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('admin_posts')
    context={'form': post_form}
    return render(request, 'admin/add_post.html', context)
    
def postDel(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('Admin_posts')
###########

def adminUsers(request):
    users = user.objects.all()
    context = { "object_list" : users}
    return render(request,'admin/users.html', context)

def userBlock(request, user_id):
    user1 = user.objects.get(id=user_id)
    user1.is_active= not user1.is_active
    user1.save()
    return redirect('admin_users')

def userPromote(request, user_id):
    user1 = user.objects.get(id=user_id)
    user1.is_superuser= not user1.is_superuser
    user1.save()
    return redirect('admin_users')

########## categories

def adminCategories(request): 
    cats = Category.objects.all()
    context = { "object_list" : cats}
    return render(request,'admin/categories.html', context)

def addCategory(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('categ-page')
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'admin/add_category.html', context)

def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    categotyForm = CategoryForm(instance=category)

    if request.method =='POST':
        categotyForm = CategoryForm(request.POST,instance=category)
        if categotyForm.is_valid():
            categotyForm.save()
            return redirect('categ-page')
    context={'form': categotyForm}
    return render(request, 'admin/add_category.html', context)
   
def categoryDelete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categ-page')

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'admin/article_details.html'

