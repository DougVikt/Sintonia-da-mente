from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from cadastro_app.models import Pacientes , Profissionais 


def check_authenticate(name, password):
    try:
        paciente = Paciente.objects.get(username=name)
        if paciente.password == password:
            return paciente
    except Paciente.DoesNotExist:
        pass

    try:
        profissional = Profissional.objects.get(username=name)
        if profissional.password == password:
            return profissional
    except Profissional.DoesNotExist:
        pass

    return None



def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = check_authenticate(name, password)  # Chama a função de autenticação

        if user is not None:
            # Verifica se o usuário esta na tabela Paciente ou Profissional
            if isinstance(user, Pacientes):
                messages.success(request, 'Login realizado com sucesso!.')
                return redirect('home_user')
            elif isinstance(user, Profissionais):
                messages.success(request, 'Login como Profissional bem-sucedido.')
                return redirect('home_specialist') 
        else:
            messages.error(request, 'Email ou senha incorreto !') 

    return render(request, 'login.html')





