from unicodedata import name
from xml.etree.ElementInclude import include
from django import urls
from django.urls import path
from . import views
from django.contrib import auth

urlpatterns = [
    path('login/', views.user_login, name='login'),

]