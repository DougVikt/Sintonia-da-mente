from django.contrib import admin
from .models import ReviewsUser, Consultations, DoctorAvailability

# registro dos modelos no admin do Django
admin.site.register(ReviewsUser)
admin.site.register(Consultations)
admin.site.register(DoctorAvailability)