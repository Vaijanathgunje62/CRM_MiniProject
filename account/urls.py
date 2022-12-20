from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TemplateView.as_view(template_name='homepage.html') ,name='homepage'),
    path('register/',SignUpView.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path("logout", LogoutView.as_view(next_page='account:homepage'), name= "logout"),
]