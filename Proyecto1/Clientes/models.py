from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.IntegerField()


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=50)
    precio = models.FloatField()


class Sucursal(models.Model):
    direccion = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    


