from django.shortcuts import render ,redirect
from django.contrib.auth import logout

# Create your views here.
def home_user(request):
    is_connected = "user"
    return render(request , 'page/home_user.html',{'is_connected':is_connected})

def logout_user(request):
    logout(request)
    return redirect('home')