# meu_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrossel, name='carrossel'),
]