from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta
from .models import Consultations as Consult ,Patients ,Professionals
import calendar


def month_text(month:int)->str:
    months = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    return months[month-1]

@login_required
def home_user(request, id , month ,year):
    user = get_object_or_404(User , id=id ) 
    patient = get_object_or_404(Patients , auth_user=user)
    consults = Consult.objects.filter(user_id=patient)
    consult_specialist = consults.values('specialist_id').distinct()
    id_specialist = set()
    for spe in consult_specialist:
        id_specialist.add(spe['specialist_id'])
        specialists = Professionals.objects.filter(id__in=id_specialist)
    if year == 1:
        month=datetime.now().month 
        year=datetime.now().year
    list_weeks = calendar.monthcalendar(year,month) 
    
    # Calcular o mês anterior e o próximo mês
    prev_month = (datetime(year, month, 1) - timedelta(days=1)).month
    prev_year = (datetime(year, month, 1) - timedelta(days=1)).year
    next_month = (datetime(year, month, 28) + timedelta(days=4)).month
    next_year = (datetime(year, month, 28) + timedelta(days=4)).year      
    date_list ={ 
        'text_month':month_text(month) ,
        'month':month,
        'year':year,
        'prev_month':prev_month,
        'prev_year':prev_year,
        'next_month':next_month,
        'next_year':next_year,
    }
    today = timezone.now()
    return render(request , 'page/home_user.html',context={
        'patient':patient,
        'is_connected': "user",
        'list_weeks': list_weeks,
        'date_list':date_list,
        'consults':consults,
        'specialists':specialists,
        'today':today
        
    })

def logout_user(request):
    logout(request)
    return redirect('home')