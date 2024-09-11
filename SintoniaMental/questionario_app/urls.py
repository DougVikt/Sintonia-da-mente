from django.urls import path
from . import views

urlpatterns = [
    path('questionario_app/', views.quest, name='quest'),
    path('questionario_app/quest_usuario', views.quest_user, name='quest_user'),
    
]