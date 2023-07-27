from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page , name='homepage'),
    path('auto_login/', views.auto_login, name='auto_login'),
    path('manual_login/', views.manual_login, name='manual_login'),
    path('home/', views.home_page, name='home'),
    path('change_credentials/', views.change_user_info, name='change_user_info'),
]