from django.contrib import admin
from .models import Pacientes , Profissionais

# Register your models here.
admin.site.register(Pacientes)
admin.site.register(Profissionais)