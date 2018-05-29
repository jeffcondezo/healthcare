from django import forms

# Model import-->
from .models import Paciente
# Model import<--


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
