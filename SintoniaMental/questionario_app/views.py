from django.shortcuts import render
from .perg_alter import * 



def quest(request):
    return render(request, 'questionario.html') 

def quest_user(request):
    context = {
        'perguntas': perguntas_usu,
        'alternativas': alternativas
    }
    return render(request, 'quest_usuario.html', context)

def quest_pais(request):
    context = {
        'perguntas':perguntas_pais,
        'alternativas':alternativas
    }
    return render(request,'quest_pais.html' , context)


def quest_prof(request):
    context = {
        'perguntas':perguntas_prof,
        'alternativas':alternativas
    }
    return render(request,'quest_prof.html' , context)

def resultado(request):
    return render(request,'resultado.html')