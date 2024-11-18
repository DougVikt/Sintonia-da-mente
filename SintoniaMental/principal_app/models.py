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
    images = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.title
    