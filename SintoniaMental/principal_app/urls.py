# meu_app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path("help/", views.help , name="help"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)