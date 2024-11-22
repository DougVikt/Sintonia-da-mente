from django.shortcuts import render
from .models import FaqBank , ContentTips

# Create your views here.
def home(request):
    tips_random = ContentTips.objects.order_by('?')[:2] # pega 2 tips aleatorios do banco
    return render(request, "pages/home.html", {"tips":tips_random})

def help(request):
    questions = FaqBank.objects.all() # pega todos os resultados
    return render(request , "pages/help.html" , {'questions':questions})