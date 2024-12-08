from django.shortcuts import render


def quest(request):
    return render(request, 'pages_quest/quest_screening.html') 


def quest_user(request):
    return render(request, 'pages_quest/quest_usuario.html')


def quest_pais(request):
    return render(request,'pages_quest/quest_pais.html' )


def quest_prof(request):
    return render(request,'pages_quest/quest_prof.html' )


def resultado(request):
    return render(request,'pages_quest/end_result.html')