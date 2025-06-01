from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta
from register_app.models import Patients ,Professionals
from user_connections.models import Consultations as Consult
import calendar


def month_text(month:int)->str:
    months = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    return months[month-1]

@login_required
def home_user(request, id , month ,year):
    # Obter o usuário com base no ID fornecido ou retornar 404 se não encontrado
    user = get_object_or_404(User, id=id)
    # Obter o paciente associado ao usuário autenticado ou retornar 404 se não encontrado
    patient = get_object_or_404(Patients, auth_user=user)
    # Obter todas as consultas associadas ao paciente
    consults = Consult.objects.filter(user_id=patient).order_by('date')
    # Obter os IDs dos especialistas das consultas do paciente, garantindo que sejam únicos
    consult_patient = consults.values('specialist_id').distinct()
    # Criar um conjunto para armazenar os IDs dos especialistas
    id_specialist = set()
    # Iterar sobre os especialistas únicos das consultas do paciente
    for spe in consult_patient:
        id_specialist.add(spe['specialist_id'])
        # Filtrar os profissionais com base nos IDs dos especialistas
        specialists = Professionals.objects.filter(id__in=id_specialist)
    # objeto de todos os especialistas
    specialists_all = Professionals.objects.all()
    # Se o ano for 1, definir o mês e o ano atuais
    if year == 1:
        month = datetime.now().month 
        year = datetime.now().year
    # Obter a lista de semanas do mês e ano fornecidos
    list_weeks = calendar.monthcalendar(year, month)
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
        'specialists_all':specialists_all,
        'today':today,
        
    })

# função e logut do usuário
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')