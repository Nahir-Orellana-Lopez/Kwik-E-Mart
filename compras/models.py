from django.db import models
from datetime import datetime

class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    precio_unitario = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return(f"""
        Nombre : {self.nombre}
        Marca: {self.marca}
        Precio: $ {self.precio_unitario}
        Categoria: {self.categoria}
        """+"\n")
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    fecha_ultima_compra = models.DateField(default=datetime.now())
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return(f"""
        Nombre : {self.nombre}
        Email: {self.email}
        Fecha de última compra: {self.fecha_ultima_compra}
        """+"\n")

class ItemCarrito(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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