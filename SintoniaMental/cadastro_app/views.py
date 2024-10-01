from django.shortcuts import render , redirect
from .models import Usuario

def cads_lite_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        fone = request.POST.get('fone')
        senha =  request.POST.get('senha')
        usuario = Usuario(
            nome=nome, email=email, fone=fone )
        usuario.cripto_senha(senha)
        usuario.save()
        return redirect('usuario/simplificado.html')
        
    
    return render(request , 'usuario/simplificado.html')


def cads_lite_prof(requst):
    return render(requst , 'profissional/simplificado.html')