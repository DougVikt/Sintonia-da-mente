from django.db import models
from django.contrib.auth.models import User

class MasterUser(models.Model):
    
    class Meta():# clase que define metadados , no caso define a classe MasterUser como uma classe modelo
        abstract = True
        
    
    auth_user= models.OneToOneField(User , on_delete=models.CASCADE)
    # cria um campo em comum com o user do django , ligação um para um 
    name = models.CharField( max_length=50)
    fone = models.CharField(max_length=15)
    date_birth = models.DateField()
    photo_perfil = models.ImageField(upload_to=f"photo_profile/{name}" , null=True , blank=True)
        
    # função para retornar o nome na pagina de admin    
    def __str__(self):
        return self.name



class Patients(MasterUser):
    class Meta:
        db_table = 'patients'
        managed = True
        verbose_name = 'Patients'
        verbose_name_plural = 'Patients'
        ordering = ['id']
    pass
    
        
class Professionals(MasterUser):
    class Meta:
        db_table = 'professionals'
        managed = True
        verbose_name = 'Professionals'
        verbose_name_plural = 'Professionals'
        ordering = ['id']
        
    register = models.CharField(max_length=80)
    specialty = models.CharField(max_length=50 , null=False , blank=True ,default=None) 
    # campo para indicar a especialidade
    verification = models.BooleanField(default=False , null=False) 
    # para definir se ja foi confirmado se e realmente um especialista 
    pass
        