from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta
from .models import Consultations as Consult



@login_required
def home_user(request, id , year=datetime.now().year , month=datetime.now().month):
    patient = get_object_or_404(User , id=id ) 
    primary_day = datetime(year,month,1)# primeiro dia do mês
    last_day = (primary_day + timedelta(days=31)).replace(day=1) - timedelta(days=1) # último dia do mês
    primary_week = [day for day in range(primary_day.weekday())] # dias iniciais da semana que faltam
    last_week = [day for day in range(last_day.weekday(),-1)] # dias finais da semana que faltam
    consults = Consult.objects.filter(user=id, date__range=[primary_day , last_day])
    days_month = list(range(1,last_day.day+1))
    return render(request , 'page/home_user.html',context={
        'patient':patient,
        'consults':consults,
        'year':year,
        'month':month,
        'days_month':days_month,
        'primary_week':primary_week,
        'last_week':last_week,
        'is_connected': "user"
    })

def logout_user(request):
    logout(request)
    return redirect('home')