from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Patients,Professionals
from django.contrib import messages


def register_lite_user(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        password = request.POST.get('password')
        date_birth = request.POST.get("datebirth")
        
        object_user = Patients.objects
        
        if object_user.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_user.filter(name=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                patient = object_user.create(
                    name=name,
                    email=email,
                    date_birth=date_birth,
                    fone=fone,  
                    password=password
                )
                patient.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect('home')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar !")
                print(e)
                
    return render(request , 'pages_user/register_user.html')


def register_lite_prof(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        date_birth = request.POST.get("datebirth")
        password = request.POST.get('password')
        crm = request.POST.get('register')
        
        object_specialist = Professionals.objects
    
        if object_specialist.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_specialist.filter(name=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                specialist = object_specialist.create(
                    auth_user = name,
                    name=name,
                    email=email,
                    fone=fone,  
                    date_birth=date_birth,
                    password=password,
                    register=crm
                )
                specialist.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect('home')
            except Exception as e:
                messages.error(request,"Erro ao cadastrar !")
                
    is_specialist = True
    
    return render(request , 'pages_specialist/register_specialist.html',{"is_specialist":is_specialist})


