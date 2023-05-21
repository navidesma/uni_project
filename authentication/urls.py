from django.urls import path
from .views import login_page, logout_view, create_user

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', create_user, name='sign_up')
]

