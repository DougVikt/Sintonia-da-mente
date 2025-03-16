from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta
#from .model.area_user_app import Patients ,Professionals
import calendar

@login_required
def home_specialist(request , id):
    user = get_object_or_404(User, pk=id)
    specialist = get_object_or_404(Professionals , user=user)
    consultations = Consult.objects.filter(professional=specialist)
    return render(request , 'home_specialist.html' )

# função e logut do usuário
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')