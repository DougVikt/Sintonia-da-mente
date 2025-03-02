from django.urls import path
from . import views

urlpatterns = [
    path('', views.quest, name='quest'),
    path('quest_user/', views.quest_user, name='quest_user'),
    path('quest_parent/' , views.quest_parent, name="quest_parent"),
    path("quest_teacher/",views.quest_teacher , name='quest_teacher'),
    path("end_result/",views.end_result , name='end_result'),
    
]