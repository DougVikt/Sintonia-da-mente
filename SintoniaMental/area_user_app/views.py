from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout  
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home_user(request, id):
    patient = get_object_or_404(User , id=id)
    return render(request , 'page/home_user.html',{'patient':patient,'is_connected': "user"})

def logout_user(request):
    logout(request)
    return redirect('home')