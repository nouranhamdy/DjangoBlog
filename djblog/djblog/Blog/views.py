from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from .serializer import UserSerializer
#auth imports.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#REST_api imports#
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

from .models import Post
# Create your views here.
# @login_required(login_url='login')
# def home(request):
#     users = User.objects.all()
#     return HttpResponse(users)


def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                msg = 'User registered successfully! ' + form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'form': form}
        return render(request, 'Blog/register.html', context)


def loginPg(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
        return render(request, 'Blog/login.html')


def signoutPg(request):
    logout(request)
    return redirect('login')


@api_view(['GET'])
def apiAllUsers(request):
    users = User.objects.all()
    st_ser = UserSerializer(users, many=True)
    return Response(st_ser.data)
#
# class HomeView(ListView):
#     model = Post
#     template_name = 'Blog/home.html'
#     ordering = ['-post_date']
    #ordering = ['-id']
def PostView(request):
    context ={
        'title':'Home Page',
        'post': Post.objects.all()
    }
    # template_name = 'Blog/home.html'
    return render(request,'Blog/home.html',context)

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return  render(request,'Blog/categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Blog/add_post.html'
    #fields = '__all__'
    #fields = ('title','body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'Blog/add_category.html'
    fields = '__all__'
    #fields = ('title','body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'Blog/update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blog/delete_post.html'
    success_url = reverse_lazy('home')