# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('otp/', views.otp, name='otp'),
    path('rules/', views.rules, name='rules'),
    path('main_test/', views.main_test, name='main_test'),
    path('calculate_result/', views.calculate_result, name='calculate_result'),
]
