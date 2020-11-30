from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('user/', views.user, name='user'),
    path('tabel/', views.tabel, name='tabel'),
    path('icon/', views.icon, name='icon'),
    path('typo/', views.typo, name='typo'),
    # path('tampilguru/', views.tampilguru, name='pengajar'),
    # path('detailguru/', views.detailguru, name='gdetail'),
    # path('detailmurid/', views.detailmurid, name='mdetail'),

]