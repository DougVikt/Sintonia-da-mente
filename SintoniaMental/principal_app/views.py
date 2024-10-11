from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated :
        nome_usuario = request.user.username
    else :
        nome_usuario = ""
    return render(request, 'home.html', {'nome_usuario' :nome_usuario})

def help(request):
    return render(request , "help.html")