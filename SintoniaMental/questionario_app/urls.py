from django.urls import path
from . import views

urlpatterns = [
    path('questionario_app/', views.quest, name='quest'),
    path('questionario_app/quest_user', views.quest_user, name='quest_user'),
    path('questionario_app/quest_pais' , views.quest_pais, name="quest_pais"),
    path("questionario_app/quest_prof",views.quest_prof , name='quest_prof'),

    
]