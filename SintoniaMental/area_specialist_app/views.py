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
def home_specialist(request, id , month ,year):
    # Obter o usuário com base no ID fornecido ou retornar 404 se não encontrado
    user = get_object_or_404(User, id=id)
    # Obter o profissional associado ao usuário autenticado ou retornar 404 se não encontrado
    specialist = get_object_or_404(Professionals, auth_user=user)
    # Obter todas as consultas associadas ao profissional por ordem decrescente de data
    consults = Consult.objects.filter(user_id=specialist).order_by('date')
    # Obter os IDs dos pacientes que ja teve consulta com o especialista 
    consult_pacients = Consult.objects.values('user').filter(specialist=specialist)
    if consult_pacients:
        # Criar um dicionario para armazenar os IDs dos pacientes com as consultas mais recentes
        recents_patients = {}
        # Iterar sobre os IDs dos pacientes e obter a consulta mais recente de cada um
        for id_pacients in consult_pacients:
            recents_patients[id_pacients] = Consult.objects.filter(user=id_pacients).order_by('-date').first()
            
    else:
        # Se não houver consultas recentes , definir como boolean False
        recents_patients = False
    # ------- CRIA A LOGICA DO CALENDARIO ------ 
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
    return render(request , 'page/home_specialist.html',context={
        'specialist':specialist,
        'is_connected': "specialist" ,
        'list_weeks': list_weeks,
        'date_list':date_list,
        'consults':consults,
        'recents_patients':recents_patients,
        
        'today':today,
        
    })

# função e logut do usuário
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')