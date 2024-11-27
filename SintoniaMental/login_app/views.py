from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from cadastro_app.models import Pacientes , Profissionais 


# def custom_authenticate(name, password):
#     try:
#         paciente = Paciente.objects.get(username=name)
#         if paciente.password == password:
#             return paciente
#     except Paciente.DoesNotExist:
#         pass

#     try:
#         profissional = Profissional.objects.get(username=name)
#         if profissional.password == password:
#             return profissional
#     except Profissional.DoesNotExist:
#         pass

#     return None

# def login_view(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         password = request.POST['password']
#         user = custom_authenticate(name, password)
#         if user is not None and user == paciente:
#             # Logar o usuário
#             login(request, user)
#             return redirect('home')  # Redirecionar para a página inicial
#         else:
#             messages.error(request, 'Credenciais inválidas.')
#     return render(request, 'login.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = custom_authenticate(username, password)  # Chama a função de autenticação

#         if user is not None:
#             # Verifica se o usuário é um Paciente ou um Profissional
#             if isinstance(user, Paciente):
#                 # O usuário é um Paciente
#                 messages.success(request, 'Login como Paciente bem-sucedido.')
#                 # Aqui você pode redirecionar para uma página específica para Pacientes
#                 return redirect('home_paciente')  # Exemplo de redirecionamento
#             elif isinstance(user, Profissional):
#                 # O usuário é um Profissional
#                 messages.success(request, 'Login como Profissional bem-sucedido.')
#                 # Aqui você pode redirecionar para uma página específica para Profissionais
#                 return redirect('home_profissional')  # Exemplo de redirecionamento
#         else:
#             messages.error(request, 'Credenciais inválidas.')  # Mensagem de erro se falhar

#     return render(request, 'login.html')







def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']   
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None :
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