from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_app', views.casd_lite , name='casd_lite'),
]
