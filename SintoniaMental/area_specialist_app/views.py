from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
#from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from datetime import datetime ,timedelta
#from .model.register_app import Patients ,Professionals


@login_required
def home_specialist(request , id):
    user = get_object_or_404(User, pk=id)
  
    return render(request , 'page/home_specialist.html', context={
        'is_connected': "specialist",
    })

# função e logut do usuário
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')