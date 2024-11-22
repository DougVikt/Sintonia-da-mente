from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user , name='login_user'),
    path('login_specialist/', views.login_specialist , name='login_specialist'),
    
   
]