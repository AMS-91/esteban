from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

urlpatterns = [
    path('/', views.user_list, name="user_list"),
    path('join/', views.sign_up, name="sign_up"),
    path('login/', views.sign_in, name="sign_in"),
]
