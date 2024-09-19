from django.shortcuts import render




def quest(request):
    return render(request, 'questionario.html') 

def quest_user(request):
    
    return render(request, 'quest_usuario.html')

def quest_pais(request):
    
    return render(request,'quest_pais.html' )


def quest_prof(request):
    
    return render(request,'quest_prof.html' )

def resultado(request):
    return render(request,'resultado.html')