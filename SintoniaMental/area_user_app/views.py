from django.shortcuts import render

# Create your views here.
def home_user(request):
    is_connected = "user"
    return render(request , 'page/home_user.html',{'is_connected':is_connected})