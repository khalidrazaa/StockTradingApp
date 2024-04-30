from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
import re

# Create your views here.

def landingbase(request):
    return render(request, "landingbase.html")

def landing(request):
    return render(request, "landing.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already taken")
            return redirect('/register/')

        try:
            user = User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email    = email,
                    password = password,
                    )

            user.set_password(password)
            user.save()
            return redirect('/login/')

        except IntegrityError:
            messages.error(request, "An error occurred while registering. Please try again.")
            return redirect('/register/')

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("username :", username)
        print("Password :", password)
        
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)

        if user is not None:
            login(request, user)
            return redirect('/portfolio/')
        
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message':error_message})
        
    return render(request, "login.html")
