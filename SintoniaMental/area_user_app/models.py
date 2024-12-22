from django.db import models
from django.contrib.auth.models import User 
from register_app.models import Professionals

# Create your models here.
class ReviewsUser(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    id_specialist = models.ForeignKey(Professionals , on_delete=models.CASCADE)
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