from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    home_page = True
    return render(request, "pages/home.html", {'home_page':home_page})

def help(request):
    return render(request , "pages/help.html")