from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_lite_user , name='register_lite_user'),
    path('register_specialist/', views.register_lite_prof , name='register_lite_prof'),
   
]
