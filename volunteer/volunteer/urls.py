"""volunteer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from messaging.views import home, room

urlpatterns = [
    #Admin URLs
    path('admin/', admin.site.urls),

    #Home URLs
    path('', include('home.urls')),

    #Accounts URLs
    path('accounts/', include('accounts.urls')),

    #Messaging URLs
    path('room/', include('messaging.urls')),

    #Clubs URLs
    path('clubs/', include('clubs.urls')),
]
