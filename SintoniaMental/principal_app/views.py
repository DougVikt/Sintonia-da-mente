from django.shortcuts import render
from .models import FaqBank , ContentTips

# Create your views here.
def home(request):
    tips = ContentTips.objects.all()
    return render(request, "pages/home.html", {"tips":tips})

def help(request):
    questions = FaqBank.objects.all() # pega todos os resultados
    return render(request , "pages/help.html" , {'questions':questions})