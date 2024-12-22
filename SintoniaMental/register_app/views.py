from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Patients,Professionals
from django.contrib import messages

object_user = User.objects

def register_user(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        password = request.POST.get('password')
        date_birth = request.POST.get("datebirth")
      
        if object_user.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_user.filter(username=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                user = object_user.create_user(username=email, first_name=name,password=password)
                user.save()
                patient = Patients.objects.create(
                    auth_user = user,
                    name=name,
                    date_birth=date_birth,
                    fone=fone,  
                )
                patient.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect(f'patient/home_user/{user.id}/')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar !")
                
    return render(request , 'pages_user/register_user.html')


def register_prof(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        date_birth = request.POST.get("datebirth")
        password = request.POST.get('password')
        crm = request.POST.get('register')        
        
        if object_user.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado !")
        elif object_user.filter(username=name).exists():
            messages.error(request, "Nome ja cadastrado !")
        else :
            try:
                user = object_user.create_user(username=email,first_name=name ,password=password)
                user.save()
                specialist = Professionals.objects.create(
                    auth_user = user,
                    name=name,
                    fone=fone,  
                    date_birth=date_birth,
                    register=crm
                )
                specialist.save()
                messages.error(request, "Cadastro realizado com sucesso !")
                return redirect('home')
            except Exception as e:
                user.delete()
                messages.error(request,"Erro ao cadastrar !")
                
    is_specialist = True
    
    return render(request , 'pages_specialist/register_specialist.html',{"is_specialist":is_specialist})


