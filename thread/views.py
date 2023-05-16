from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Thread
from community.models import Community
from .forms import ThreadForm
from django.contrib.auth.models import User


@login_required()
def main(request: HttpRequest):
    threads = Thread.objects.all()
    return render(request, 'thread/main.html', {"threads": threads})


@login_required()
def create_thread(request: HttpRequest):
    communities = Community.objects.all()
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            community = Community.objects.get(id=form.cleaned_data['community'])
            thread = Thread(creator_id=user, title=form.cleaned_data['title'],
                            content=form.cleaned_data['content'], community=community)
            thread.save()
            return redirect('main-page')
        else:
            return render(request, 'thread/new-thread.html', {'form': form, 'message': "فرم نادرست است",
                                                              'communities': communities})

    return render(request, 'thread/new-thread.html', {"form": form, 'communities': communities})
