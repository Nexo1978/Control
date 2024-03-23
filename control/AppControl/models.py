from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField ()
    cantidad_en_stock = models.PositiveIntegerField()
   
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.CharField(max_length=100)
    productos_vendidos = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()

