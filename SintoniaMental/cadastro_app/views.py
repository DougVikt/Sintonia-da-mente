from django.shortcuts import render , redirect
from .models import Pacientes,Profissionais
from django.contrib import messages


def register_lite_user(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        password = request.POST.get('password')
        
        object_user = Pacientes.objects
        
        if object_user.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_user.filter(name=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                patient = object_user.create(
                    name=name,
                    email=email,
                    fone=fone,  
                    password=password
                )
                patient.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect('home_user')
            except Exception as e:
                messages.error(request, f"Erro ao cadastrar !")
                
    return render(request , 'pages_user/register_user.html')


def register_lite_prof(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        password = request.POST.get('password')
        crm = request.POST.get('register')
        
        object_specialist = Profissionais.objects
    
        if object_specialist.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_specialist.filter(name=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                specialist = object_specialist.create(
                    name=name,
                    email=email,
                    fone=fone,  
                    password=password,
                    register=crm
                )
                specialist.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect('home_specialist')
            except Exception as e:
                messages.error(request,"Erro ao cadastrar !")
                
    is_specialist = True
    
    return render(request , 'pages_specialist/register_specialist.html',{"is_specialist":is_specialist})


