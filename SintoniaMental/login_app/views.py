from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from cadastro_app.models import Pacientes , Profissionais 


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']   
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and isinstance(user, Pacientes):
            login(request, user)
            return redirect('home_user')
        else:
            messages.error(request, 'Email ou senha invalidos !')
                                                
    return render(request, 'login.html')

def login_specialist(request):
    if request.method == 'POST':
        username = request.POST['username']   
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and isinstance(user, Profissionais):
            login(request, user)
            return redirect('home_specialist')
        else:
            messages.error(request, 'Email ou senha invalidos !')
                                                
    return render(request, 'login.html')