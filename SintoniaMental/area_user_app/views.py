from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout
from register_app.models import Patients

# Create your views here.
def home_user(request, id):
    patient = get_object_or_404(Patients , id=id)
    return render(request , 'page/home_user.html',{'patient':patient})

def logout_user(request):
    logout(request)
    return redirect('home')