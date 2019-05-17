from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


def contact(request):
    return render(request=request,
                  template_name='main/contact.html')


def incidence(request):
    return render(request=request,
                  template_name='main/incidence.html')


def profile(request):
    return render(request=request,
                  template_name='main/profile.html')


def login(request):

    return render(request=request,
                  template_name='login.html',
                  context={'form': form})


def register(request):
    print("Register funct")
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('main:homepage')
    else:
        form = UserRegisterForm()
    return render(request=request,
                  template_name='register.html',
                  context={'form': form})
