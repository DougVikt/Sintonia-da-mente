from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_app/usuario', views.cads_lite_user , name='cads_lite_user'),
    path('cadastro_app/profissional', views.cads_lite_prof , name='cads_lite_prof'),
    path('cadastro_app',views.login ,name='login'),
]
