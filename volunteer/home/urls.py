from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from home.views import HomeView, LogView
from accounts.views import view_post

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('log', LogView.as_view(), name='log'),
    path('post/<str:pk>/', view_post, name="view_post"),
]
