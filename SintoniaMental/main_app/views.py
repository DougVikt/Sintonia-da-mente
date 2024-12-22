from django.shortcuts import render
from .models import FaqBank , ContentTips 
from area_user_app.models import ReviewsUser
import random

# Create your views here.
def home(request):
    try:
        content_tips = ContentTips.objects.all()
        reviews_user = ReviewsUser.objects.all()
        if content_tips.exists():
            tips_random = random.sample(list(content_tips)) 
            # pega todos tips e armazena na lista depois o embaralha
        else :
            tips_random = ['nada aqui' , 'nada aqui']
        if reviews_user.exists():
            reviews_random = random.sample(list(reviews_user))
        else:   
            reviews_random = ['nada aqui']
            
        context = {
            "tips1":tips_random[0],
            "tips2":tips_random[1],
            "reviews":reviews_random,
        }
        return render(request, "pages/home.html", context)
    except Exception as e:
        context = {
            "tips1":'Algo deu errado ',
            "tips2":'Algo deu errado',
            "reviews":'Algo deu errado',
        }
        return render(request, "pages/home.html", context)

def help(request):
    questions = FaqBank.objects.all() # pega todos os resultados
    return render(request , "pages/help.html" , {'questions':questions})