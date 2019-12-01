from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from lobby.views import lobby
from home.views import about, creators


urlpatterns = [
    path('', lobby, name="lobby"),
    path('about/', about, name='about'),
    path('creators/', creators, name='creators')
]
