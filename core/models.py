from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    portada = models.ImageField(upload_to="productos", null = True, blank = True)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descipcion = models.TextField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class carrito(models.Model):
    nombre = models.CharField(max_length=50)
    portada = models.ImageField(null = True, blank = True)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    descipcion = models.TextField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
