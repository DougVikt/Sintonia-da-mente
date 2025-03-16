from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta
from .models import Consultations as Consult ,Patients ,Professionals
import calendar



# função e logut do usuário
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')