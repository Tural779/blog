from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('blogpage', views.blogpage, name='blogpage'),
    path('addblogpage', views.addblogpage, name='addblogpage'),
]
