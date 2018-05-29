from django.db import models
from maestro.models import Distrito


# Create your models here.
class Paciente(models.Model):
    CIVIL_CHOICES = (
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado'),
    )
    nombres = models.CharField(max_length=250)
    apepaterno = models.CharField(max_length=200)
    apematerno = models.CharField(max_length=200)
    fechanacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=9)
    dni = models.CharField(max_length=8, null=True, blank=True)
    carne = models.CharField(max_length=10, null=True, blank=True)
    procedencia = models.ForeignKey(Distrito, on_delete=models.PROTECT, related_name='procedencia_paciente', null=True,
                                    blank=True)
    residencia = models.ForeignKey(Distrito, on_delete=models.PROTECT, related_name='residencia_paciente', null=True,
                                   blank=True)
    archivo = models.CharField(max_length=6, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    estadocivil = models.CharField(max_length=1, choices=CIVIL_CHOICES, null=True, blank=True)
    grupo = models.CharField(max_length=2, null=True, blank=True)
    factor = models.CharField(max_length=1, null=True, blank=True)
