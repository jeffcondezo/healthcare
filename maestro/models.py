from django.db import models


# Create your models here.
class Pais(models.Model):
    descripcion = models.CharField(max_length=200)


class Departamento(models.Model):
    descripcion = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)


class Provincia(models.Model):
    descripcion = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)


class Distrito(models.Model):
    descripcion = models.CharField(max_length=200)
    ubigeo = models.CharField(max_length=10)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)


class Empresa(models.Model):
    ruc = models.CharField(max_length=11)
    razonsocial = models.CharField(max_length=150)
    is_own = models.CharField(max_length=1, default='0')
    is_active = models.CharField(max_length=1, default='1')


class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    distrito = models.ForeignKey(Distrito, on_delete=models.PROTECT)
    direccion = models.TextField()
