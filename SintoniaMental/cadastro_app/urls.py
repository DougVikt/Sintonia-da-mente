from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_app/usuario', views.cads_lite , name='cads_lite'),
]
