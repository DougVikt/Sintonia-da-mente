from django.shortcuts import render , redirect
from .models import Usuarios

def cads_lite_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        senha =  request.POST.get('senha')
        usuario = Usuarios(
            nome=nome, email=email, fone=fone )
        usuario.cripto_senha(senha)
        usuario.save()
        return redirect('usuario/simplificado.html')
        
    
    return render(request , 'usuario/simplificado.html')


def cads_lite_prof(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        senha =  request.POST.get('senha')
        usuario = Usuarios(
            nome=nome, email=email, fone=fone )
        usuario.cripto_senha(senha)
        usuario.save()
        return redirect('profissional/simplificado.html')
        
    return render(request , 'profissional/simplificado.html')



def login(request):
    return render(request,'login.html')