from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate 
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        print('ok1')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request , email=email, password=password)  
        
        if user is not None:
            print('ok2')
            auth_login(request,user)
            # Verifica se o usuário esta na tabela Patients ou Professionals
            if hasattr(user, 'patients'):
                print('ok3')
                # verifica se o atributo patients esta no objeto , atributo esse criado pelo django
                messages.success(request, 'Login realizado com sucesso!.')
                return redirect('home_user' , id=user.patients.id)
            elif hasattr(user, 'professionals'):
                messages.success(request, 'Login como profissional bem-sucedido.')
                return redirect('home_specialist', id=user.professionals.id) 
        else:
            messages.error(request, 'Email ou senha incorreto !') 

    return render(request, 'login.html')





