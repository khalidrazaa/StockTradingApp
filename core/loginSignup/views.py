from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def landing(request):
    return render(request, "landing.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def landingbase(request):
    return render(request, "landingbase.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('home')  # Change 'home' to the name of your homepage URL
            else:
                # Invalid login
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid email or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})