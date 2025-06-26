from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from register_app.models import Professionals
from user_connections.models import Consultations

#@login_required
def call_consult(request, user_id=1):
    consult = get_object_or_404(Consultations, id=user_id)
    specialist = consult.specialist
    context = {
        'name_specialist': specialist.name,
        'specialty': specialist.specialty,
        'date_consult': consult,
    }
    return render(request, 'partitions/body.html', context)