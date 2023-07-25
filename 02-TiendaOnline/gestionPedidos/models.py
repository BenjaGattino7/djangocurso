from django.db import models


class Clientes (models.Model):
    nombre=models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=20, verbose_name="Telefono")

    def __str__(self) :
        return self.nombre

class Articulos (models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=25)
    precio=models.IntegerField()

    def __str__ (self) :
        return self.nombre
        

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()







  