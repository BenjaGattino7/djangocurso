from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=60)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True,blank=True)
    precio =models.FloatField()
    disponible=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre
    