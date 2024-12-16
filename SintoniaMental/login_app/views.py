from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate 
from django.contrib import messages




def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request , username=email, password=password)  

        if user is not None:
            auth_login(request,user)
            # Verifica se o usuário esta na tabela Patients ou Professionals
            if hasattr(user, 'patients'):
                # verifica se o atributo patients esta no objeto , atributo esse criado pelo django
                messages.success(request, 'Login realizado com sucesso!.')
                return redirect('home_user' , id=user.id)
            elif hasattr(user, 'professionals'):
                messages.success(request, 'Login como profissional bem-sucedido.')
                return redirect('home_specialist', id=user.id) 
        else:
            messages.error(request, 'Email ou senha incorreto !') 

    return render(request, 'login.html')





