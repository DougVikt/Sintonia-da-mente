from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nome = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    fone = models.CharField(max_length=15)
    senha = models.CharField(max_length=128)
    
    def cripto_senha(self , text_senha):
        self.senha = make_password(text_senha)