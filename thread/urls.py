from django.urls import path
from .views import main, create_thread

urlpatterns = [
    path('', main, name='main-page'),
    path('new-thread/', create_thread, name='new-thread')
]
