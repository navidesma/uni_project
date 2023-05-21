from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Thread, Comment
from community.models import Community
from .forms import ThreadForm, CommentForm
from authentication.models import ProfilePicture


@login_required()
def main(request: HttpRequest):
    threads = Thread.objects.all()
    profile_pictures = ProfilePicture.objects.all()
    return render(request, 'thread/main.html',
                  {"threads": threads, "user": request.user.id, 'profile_pictures': profile_pictures})


@login_required()
def create_thread(request: HttpRequest):
    communities = Community.objects.all()
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = Thread(creator_id=request.user.id, title=form.cleaned_data['title'],
                            content=form.cleaned_data['content'], community_id=form.cleaned_data['community'])
            thread.save()
            return redirect('main-page')
        else:
            return render(request, 'thread/new-thread.html', {'form': form, 'message': "فرم نادرست است",
                                                              'communities': communities})

    return render(request, 'thread/new-thread.html', {"form": form, 'communities': communities})


def single_thread(request: HttpRequest, thread_id: int):
    thread = Thread.objects.get(id=thread_id)
    form = CommentForm()
    return render(request, 'thread/single-thread.html', {"thread": thread, "form": form})


@login_required()
def create_comment(request: HttpRequest, thread_id: int):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                if 'parent' in form.cleaned_data:
                    comment = Comment(thread_id=thread_id, content=form.cleaned_data['content'],
                                      parent_id=form.cleaned_data['parent'], commenter_id=request.user.id)
                else:
                    comment = Comment(thread_id=thread_id, content=form.cleaned_data['content'],
                                      commenter_id=request.user.id)

                comment.save()

            except:
                threads = Thread.objects.all()
                return render(request, 'thread/main.html',
                              {"threads": threads, "user": request.user.id, 'message': "نظر ثبت نشد"})
            return redirect('single-thread', thread_id=thread_id)

        threads = Thread.objects.all()
        return render(request, 'thread/main.html',
                      {"threads": threads, "user": request.user.id, 'message': "فرم نادرست است"})

    return redirect('single-thread', thread_id=thread_id)
