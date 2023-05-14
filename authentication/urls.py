from django.urls import path
from .views import login_page, logout_view

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout')
]

