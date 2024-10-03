from django import forms 
from .models import Pacientes
from .models import Profissionais


class PacienteValidate(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ('nome', 'email', 'fone', 'senha')

class ProfisValidate(forms.ModelForm):
    class Meta:
        model = Profissionais
        fields = ('nome', 'email', 'fone', 'senha', 'registro')
        