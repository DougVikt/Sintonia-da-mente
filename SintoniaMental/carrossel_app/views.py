from django.shortcuts import render

# Create your views here.
def carrossel(request):
    return render(request, 'carrossel.html')