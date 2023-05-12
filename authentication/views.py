from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from .forms import LoginForm


def login_page(request: HttpRequest):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f'سلام {user.username}! با موفقیت وارد شدید'
            else:
                message = 'ورود با مشکل مواجه شد'
        else:
            message = "داده ها غلظ هستند"

    return render(request, 'login.html', context={'message': message, "page_title": "ورود کاربر"})
