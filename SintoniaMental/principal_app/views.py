from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# PARA PEGAR UM ID ALEATORIO E CRIAR UM CARD 

# from django.shortcuts import render
# from .models import Tabela (colocar o nome da tabela)
# import random

# def home(request):
#     num_linhas = Tabela.objects.count()
#     ids_aleatorios = random.sample(range(1, num_linhas + 1), 3)
#     objetos = Tabela.objects.filter(id__in=ids_aleatorios)
#       return render(request, 'home.html', {'objetos': objetos})

#  UMA SEGUNDA MANEIRA

#     objetos = Card.objects.all().order_by('?')[:3]
#       return render(request, 'home.html', {'objetos': objetos})
