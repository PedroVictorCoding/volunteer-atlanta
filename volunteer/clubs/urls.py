from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from .views import home, robotics, cheer_home

urlpatterns = [
    path('', home, name='clubs_homepage'),

    # Robotics Pages
    path('robotics/', robotics, name="robotics_homepage"),

    # Cheer Pages
    path('cheerleading/', cheer_home, name='cheer'),
    #path('cheerleading/equipment/', , name='cheer_equipment')
]
