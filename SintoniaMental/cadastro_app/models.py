from django.db import models
from django.contrib.auth.hashers import make_password

class Usuarios(models.Model):
    
    class Meta():# clase que define metadados , no caso define a classe Usuarios como uma classe modelo
        abstract = True
    
    name = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    fone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        # Se a senha não estiver criptografada, criptografa antes de salvar
        if self.pk is None:  # Verifica se é um novo objeto
            self.password = make_password(self.password)  # Criptografa a senha
        super().save(*args, **kwargs)
    
    
    # função para retornar o nome na pagina de admin    
    def __str__(self):
        return self.nome

class Pacientes(Usuarios):
    pass
        
        
class Profissionais(Usuarios):
    register = models.CharField(max_length=80)
    verification = models.BooleanField(default=False , null=False)
    pass
        