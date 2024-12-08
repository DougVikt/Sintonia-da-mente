from django.contrib import admin
from .models import Patients , Professionals

# Register your models here.
admin.site.register(Patients)
admin.site.register(Professionals)