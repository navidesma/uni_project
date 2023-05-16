from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Community
from .forms import CommunityForm


@login_required()
def create_community(request: HttpRequest):
    form = CommunityForm()
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = Community(name=form.cleaned_data['name'], description=form.cleaned_data['short_description'],
                                  short_description=form.cleaned_data['short_description'])
            community.save()
            return redirect('main-community')
        else:
            return render(request, 'thread/new-thread.html', {'form': form, 'message': "فرم نادرست است"})

    return render(request, 'community/new-community.html', {"form": form})


def community_view(request: HttpRequest):
    communities = Community.objects.all()

    return render(request, 'community/main.html', {'communities': communities})
