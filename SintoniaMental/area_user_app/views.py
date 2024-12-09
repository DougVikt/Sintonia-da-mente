from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User

# Create your views here.
def home_user(request, id):
    patient = get_object_or_404(User , id=id)
    return render(request , 'page/home_user.html',{'patient':patient})

def logout_user(request):
    logout(request)
    return redirect('home')