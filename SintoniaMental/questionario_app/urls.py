from django.urls import path
from . import views

urlpatterns = [
    path('', views.quest, name='quest'),
    path('quest_user', views.quest_user, name='quest_user'),
    path('quest_pais' , views.quest_pais, name="quest_pais"),
    path("quest_prof",views.quest_prof , name='quest_prof'),
    path("end_result",views.resultado , name='result'),
    
]