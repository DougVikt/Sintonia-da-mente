from django.db import models
from django.contrib.auth.models import User 
from register_app.models import Professionals , Patients

# classe de avaliações dos usuários
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
        return self.user.first_name
    
# classe de consultas dos usuários
class Consultations(models.Model):
    user = models.ForeignKey(Patients , on_delete=models.CASCADE)
    specialist = models.ForeignKey(Professionals , on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    type_consultation = models.CharField(max_length=20)
    class Meta:
        db_table = 'consultations'
        managed = True
        verbose_name = 'Consultations'
        verbose_name_plural = 'Consultations'
        ordering = ['id']
    def __str__(self):
        return self.user.first_name