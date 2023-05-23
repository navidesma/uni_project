from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Community, CommunitySubscription
from thread.models import Thread
from .forms import CommunityForm
from django.contrib import messages


@login_required()
def create_community(request: HttpRequest):
    form = CommunityForm()
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = Community(name=form.cleaned_data['name'], description=form.cleaned_data['short_description'],
                                  short_description=form.cleaned_data['short_description'])
            community.save()
            messages.success(request, "انجمن با موفقیت ایجاد شد")
            return redirect('main-community')
        else:
            messages.error(request, "فرم نادرست است")

    return render(request, 'community/new-community.html', {"form": form})


@login_required()
def community_view(request: HttpRequest):
    communities = Community.objects.all()

    return render(request, 'community/main.html', {'communities': communities, 'user': request.user.id})


@login_required()
def single_community_view(request: HttpRequest, community_id: int):
    community = Community.objects.get(id=community_id)

    return render(request, 'community/single-community.html', {'community': community, 'user': request.user.id})


@login_required()
def subscribe(request: HttpRequest, community_id: int):
    already_subscribed = CommunitySubscription.objects.filter(user_id=request.user.id, community_id=community_id)
    if not already_subscribed:
        subscription = CommunitySubscription(community_id=community_id, user_id=request.user.id)
        subscription.save()

    return redirect('main-community')


@login_required()
def unsubscribe(request: HttpRequest, community_id: int):
    try:
        subscription = CommunitySubscription.objects.get(user_id=request.user.id, community_id=community_id)
        subscription.delete()
    except ObjectDoesNotExist:
        pass

    return redirect('main-community')
