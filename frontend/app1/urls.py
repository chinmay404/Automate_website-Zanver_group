from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage , name='hmomepage'),
    path('auto_login/', views.auto_login, name='auto_login'),
]