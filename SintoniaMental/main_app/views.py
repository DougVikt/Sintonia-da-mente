from django.shortcuts import render
from .models import FaqBank , ContentTips
import random

# Create your views here.
def home(request):
    tips_random = list(ContentTips.objects.all()) 
    # pega todos tips e armazena na lista
    random.shuffle(tips_random)
    # emparalha todos os resultados 
    return render(request, "pages/home.html", context={"tips1":tips_random[0],"tips2":tips_random[1]})

def help(request):
    questions = FaqBank.objects.all() # pega todos os resultados
    return render(request , "pages/help.html" , {'questions':questions})