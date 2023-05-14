from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


def login_page(request: HttpRequest):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main-page')
            else:
                message = 'ورود با مشکل مواجه شد'
        else:
            message = "داده ها غلظ هستند"

    return render(request, 'authentication/login.html', context={'message': message})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login')
