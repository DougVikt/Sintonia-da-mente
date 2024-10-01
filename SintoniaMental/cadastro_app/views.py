from django.shortcuts import render

def cads_lite(request):
    return render(request , 'usuario/simplificado.html')

