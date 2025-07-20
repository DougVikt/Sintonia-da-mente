from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home_specialist/<int:id>/<int:month>/<int:year>/', views.home_specialist, name='home_specialist'),
    path('logout/',views.logout_user , name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)