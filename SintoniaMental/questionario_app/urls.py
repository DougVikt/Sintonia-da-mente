from django.urls import path
from . import views

urlpatterns = [
    path('questionario_app/', views.quest, name='quest'),
]