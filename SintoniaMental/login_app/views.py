from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login , authenticate 
from django.contrib import messages
from django.conf import settings
from django.views.decorators.cache import never_cache


@never_cache
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        remember = request.POST.get('remember')
        user = authenticate(request , username=email, password=password)  
    
        if user is not None:
            try :
                auth_login(request,user)
                # expiração do usuario 
                if remember:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE) # expira em 30 miniutos de inatividade
                else:
                    request.session.set_expiry(0) # expira quando o navegador fecha
                    
                # Verifica se o usuário esta na tabela Patients ou Professionals
                if hasattr(user, 'patients'):
                    # verifica se o atributo patients esta no objeto , atributo esse criado pelo django
                    messages.success(request, 'Login realizado com sucesso!.')
                    return redirect('home_user' , id=user.id , month=1 , year=1)
                elif hasattr(user, 'professionals'):
                    messages.success(request, 'Login como profissional bem-sucedido.')
                    return redirect('home_specialist', id=user.id) 
                else:
                    messages.error(request, 'Usuario não cadastrado !')
            except Exception as e:
                messages.error(request, 'Erro ao logar !')
        else:
            messages.error(request, 'Email ou senha incorreto !') 
        
    return render(request, 'login.html')





