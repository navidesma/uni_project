from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm
from .models import ProfilePicture
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4
from django.conf import settings

path = settings.MEDIA_ROOT


def handle_uploaded_file(file):
    file_name = f'{uuid4()}{file.name}'
    file_path = f'{path}{file_name}'
    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_name


def login_page(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main-page')
            else:
                messages.error(request, 'ورود با مشکل مواجه شد')
        else:
            messages.error(request,  'داده ها غلط هستند')

    return render(request, 'authentication/login.html')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login')


def create_user(request: HttpRequest):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['re_enter_password']:
                messages.error(request, 'رمز عبور ها یکی نیستند')

            elif User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'این نام کاربری قبلا استفاده شده')

            elif 'picture' in request.FILES:
                picture_path = handle_uploaded_file(request.FILES['picture'])

                User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                user = User.objects.get(username=form.cleaned_data['username'])
                profile_picture = ProfilePicture(user=user, profile_pic=picture_path)
                profile_picture.save()

                return redirect('login')
            elif 'picture' not in request.FILES:
                User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                user = User.objects.get(username=form.cleaned_data['username'])
                profile_picture = ProfilePicture(user=user, profile_pic="blank_user_profile.jpg")
                profile_picture.save()

                return redirect('login')
            else:
                User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                return redirect('login')

    return render(request, 'authentication/sign-up.html')
