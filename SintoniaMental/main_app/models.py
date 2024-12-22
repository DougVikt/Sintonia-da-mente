from django.db import models

class FaqBank(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    class Meta:
        db_table = 'faq_bank'
        managed = True
        verbose_name = 'FaqBank'
        verbose_name_plural = 'FaqBanks'
        ordering = ['id']
    
class ContentTips(models.Model):
    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField( upload_to='tips/', blank=True)
    alt_image = models.CharField( max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'content_tips'
        managed = True
        verbose_name = 'ContentTips'
        verbose_name_plural = 'ContentTips'
        ordering = ['id']