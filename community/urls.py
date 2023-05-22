from django.urls import path
from .views import community_view, create_community, subscribe, unsubscribe, single_community_view

urlpatterns = [
    path('', community_view, name='main-community'),
    path('new-community/', create_community, name='new-community'),
    path('subscribe/<int:community_id>/', subscribe, name='community-subscribe'),
    path('unsubscribe/<int:community_id>/', unsubscribe, name='community-unsubscribe'),
    path('community/<int:community_id>/', single_community_view, name='single-community')
]
