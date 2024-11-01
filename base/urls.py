from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login/', TokenObtainPairView.as_view()),
]

