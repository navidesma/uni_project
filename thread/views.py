from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Thread
from .forms import ThreadForm
from django.contrib.auth.models import User


@login_required()
def main(request: HttpRequest):
    threads = Thread.objects.all()
    return render(request, 'thread/main.html', {"threads": threads})


@login_required()
def create_thread(request: HttpRequest):
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            thread = Thread(creator_id=user, title=form.cleaned_data['title'],
                            content=form.cleaned_data['content'])
            thread.save()
        else:
            return render(request, 'thread/new-thread.html', {'form': form})

    return render(request, 'thread/new-thread.html', {"form": form})
