from django.db import models

# Create your models here.

class Insumo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    unidad_de_medida = models.CharField(max_length=40)
    cantidad_de_stock = models.IntegerField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_de_stock = models.IntegerField()
    otra_cosa = models.TextField()