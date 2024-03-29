"""
URL configuration for uni_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from thread.urls import main
from . import run_on_startup

urlpatterns = [
    path("", main, name="main-page"),
    path("admin/", admin.site.urls),
    path("authentication/", include("authentication.urls")),
    path("thread/", include("thread.urls")),
    path("community/", include("community.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


try:
    run_on_startup.run_on_startup()
except Exception:
    print(
        "something went wrong while creating default data,\n\n run:\n python manage.py makemigrations \nand then run:\n python manage.py migrate"
    )
