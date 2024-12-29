from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register_user/', views.register_user , name='register_user'),
    path('register_specialist/', views.register_prof , name='register_prof'),
   
]
# para adicionar o caminho das midias 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)