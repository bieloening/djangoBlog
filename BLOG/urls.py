from unicodedata import name
from xml.etree.ElementInclude import include
from django import urls
from django.urls import path
from . import views
from django.contrib import auth

urlpatterns = [
    path('', views.inicio, name='home'),
    path('postar/', views.postar, name='postar'),
    path('adicionar_informacao/', views.adicionar_informacao, name='adicionar_informacao'),
    # path('logar/', views.logar, name='logar'),
    # path('cadastrar/', views.cadastrar, name='cadastrar'),


]