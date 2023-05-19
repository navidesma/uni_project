from django.urls import path
from .views import main, create_thread, single_thread, create_comment

urlpatterns = [
    path('', main, name='main-page'),
    path('new-thread/', create_thread, name='new-thread'),
    path('thread/<int:thread_id>/', single_thread, name='single-thread'),
    path('comment/<int:thread_id>', create_comment, name='create-comment')
]
