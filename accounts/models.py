from django.db import models
from django.contrib.auth.models import User

# from datetime import datetime

# class Cliente(models.Model):
#     nombre = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200, null=True)
#     fecha_ultima_compra = models.DateField(default=datetime.now())
#     habilitado = models.BooleanField(default=True)

#     def __str__(self):
#         return(f"""
#         Nombre : {self.nombre}
#         Email: {self.email}
#         Fecha de última compra: {self.fecha_ultima_compra}
#         """+"\n")

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
