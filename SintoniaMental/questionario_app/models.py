from django.db import models

# Create your models here.



# class Question(models.Model):
#     text = models.CharField(max_length=255)
#     options = models.TextField()  # armazena as opções de resposta em formato JSON

# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     response = models.CharField(max_length=255)