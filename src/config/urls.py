"""
URL configuration for config project.

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
from django.urls import path
from django.urls.conf import include, re_path

from rest_auth.views.google import google_oauth2_login, google_oauth2_callback
from rest_auth.views.templates import login_cancelled, login_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('accounts/google/login/', google_oauth2_login, name="google_login"),
    path('accounts/google/login/callback/', google_oauth2_callback, name="google_callback"),
    path('accounts/google/login/cancelled/', login_cancelled, name='login_cancelled'),
    path('accounts/google/login/error/', login_error, name='login_error'),

    path('', include('contacts.urls')),
]
