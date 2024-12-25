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
            tips_random = random.sample(list(content_tips) , min(len(content_tips) , 2)) 
            # pega todos tips e armazena na lista depois o embaralha
        else :
            tips_random = ['nada aqui' , 'nada aqui']
        if reviews_user.exists():
            reviews_random = random.sample(list(reviews_user), min(len(reviews_user), len(reviews_user)))
        else:   
            reviews_random = ['nada aqui']
            
        context = {
            "tips":tips_random,
            "reviews":reviews_random,
        }
        print(reviews_random)
        return render(request, "pages/home.html", context)
    except Exception as e:
        print(e)
        context = {
            "tips":['Algo deu errado ','Algo deu errado '],
            "reviews":'Algo deu errado',
        }
        
        return render(request, "pages/home.html", context)

def help(request):
    questions = FaqBank.objects.all() # pega todos os resultados
    return render(request , "pages/help.html" , {'questions':questions})