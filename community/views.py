from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Community, CommunitySubscription
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

    return render(request, 'community/main.html', {'communities': communities, 'user': request.user.id})


def subscribe(request: HttpRequest, community_id: int):
    already_subscribed = CommunitySubscription.objects.filter(user_id=request.user.id, community_id=community_id)
    if not already_subscribed:
        subscription = CommunitySubscription(community_id=community_id, user_id=request.user.id)
        subscription.save()

    return redirect('main-community')


def unsubscribe(request: HttpRequest, community_id: int):
    try:
        subscription = CommunitySubscription.objects.get(user_id=request.user.id, community_id=community_id)
        subscription.delete()
    except ObjectDoesNotExist:
        pass

    return redirect('main-community')
