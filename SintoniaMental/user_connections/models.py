from django.db import models
from register_app.models import Professionals , Patients

# classe de avaliações das consultas dos usuários
class ReviewsUser(models.Model):
    user = models.ForeignKey(Patients , on_delete=models.CASCADE)
    specialist = models.ForeignKey(Professionals , on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'reviews_user'
        managed = True
        verbose_name = 'ReviewsUser'
        verbose_name_plural = 'ReviewsUsers'
        ordering = ['id']
    def __str__(self):
        return self.user.name
    
# classe de consultas dos usuários
class Consultations(models.Model):
    user = models.ForeignKey(Patients , on_delete=models.CASCADE)
    specialist = models.ForeignKey(Professionals , on_delete=models.CASCADE)
    description = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    type_consultation = models.CharField(max_length=20)
    class Meta:
        db_table = 'consultations'
        managed = True
        verbose_name = 'Consultations'
        ordering = ['id']
    def __str__(self):
        return self.user.name
    
# classe de disponibilidade dos médicos
class DoctorAvailability(models.Model):
    specialist = models.ForeignKey(Professionals, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        db_table = 'doctor_availability'
        managed = True
        verbose_name = 'Doctor Availability'
        verbose_name_plural = 'Doctor Availabilities'
        ordering = ['id']
    # função para retornar o nome do especialista e a data da disponibilidade
    def __str__(self):
        return f"{self.specialist.name} - {self.date} ({self.start_time} as {self.end_time})"