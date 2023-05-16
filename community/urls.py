from django.urls import path
from .views import community_view, create_community

urlpatterns = [
    path('', community_view, name='main-community'),
    path('new-community/', create_community, name='new-community')
]
