from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    categorias = models.CharField(null=True, blank=True, max_length=200)
    precio_unitario = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=False)
    fecha_subida = models.DateField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/articulos")

    def __str__(self):
        return(f"""
        Nombre : {self.nombre}
        Marca: {self.marca}
        Precio: $ {self.precio_unitario}
        """+"\n")

class ItemCarrito(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return(f"""
        Nombre : {self.articulo.nombre}
        Precio: $ {self.articulo.precio_unitario}
        Cantidad: {self.cantidad}
        Suma parcial : $ {self.articulo.precio_unitario*self.cantidad}
        """+"\n")
    
    def agregar(self):
        self.cantidad+=1
        
    def quitar(self):
        self.cantidad-=1