from django.shortcuts import render , redirect
from .models import Pacientes,Profissionais
from .forms import PacienteValidate,ProfisValidate

def cads_lite_user(request):
    if request.method == 'POST':
        form = PacienteValidate(request.POST)
        if form.is_valid():
            usuario = Pacientes.objects.create(
                nome = form.cleaned_data['nome'],
                email = form.cleaned_data['email'],
                fone = form.cleaned_data['fone']
            )
            usuario.cripto_senha(form.cleaned_data['senha'])
            usuario.save()
            print('foi salvo')
            return redirect('home')
    else:
        print('não foi salvo')
    
    return render(request , 'usuario/simplificado.html')


def cads_lite_prof(request):
    if request.method == 'POST':
        form = ProfisValidate(request.POST)
        if form.is_valid():
            profis = Profissionais.objects.create(
                nome = form.cleaned_data['nome'],
                email = form.cleaned_data['email'],
                fone = form.cleaned_data['fone'] )
            profis.cripto_senha(form.cleaned_data['senha'])
            profis.save()
            return redirect("home")
        
    return render(request , 'profissional/simplificado.html')



def login(request):
    return render(request,'login.html')