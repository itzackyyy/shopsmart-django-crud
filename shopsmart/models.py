from django.db import models

# Create your models here.


class Usuarios(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    edadUsuario = models.IntegerField()
    direccionUsuario = models.TextField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    


class Productos(models.Model):
    nombreProducto = models.CharField(max_length=100)
    tipoProducto = models.CharField(max_length=50)
    cantidadDisponibleProducto = models.IntegerField()
    #fecha cuando se actualiza la cantidad (próximamente xd)