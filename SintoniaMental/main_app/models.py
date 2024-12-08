from django.db import models

class FaqBank(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
class ContentTips(models.Model):
    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField( upload_to='tips/', blank=True)
    alt_image = models.CharField( max_length=200)
    
    def __str__(self):
        return self.title
    