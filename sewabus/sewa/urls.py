from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('<id>/detail/', views.detail, name='detail'),
    

]