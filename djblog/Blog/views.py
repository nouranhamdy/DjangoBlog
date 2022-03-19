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


# Create your views here.
@login_required(login_url='login')
def home(request):
    users = User.objects.all()
    return HttpResponse(users)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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
    if request.user.is_authenticated:
        return redirect('home')
    else:
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