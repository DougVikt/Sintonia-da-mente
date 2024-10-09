from django.shortcuts import render

# Create your views here.
def home_user(request):
    return render(request , 'home_user.html')