from django import forms
from .models import Articulo

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    habilitado = forms.BooleanField(initial=True, required=False)

class ArticuloFormulario(forms.Form):
    categoria = forms.CharField(max_length=200)
    nombre = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=200)
    precio_unitario = forms.FloatField()
    stock = forms.IntegerField()
    disponible = forms.BooleanField(initial=True, required=False)
    imagen = forms.ImageField(required=False, widget=forms.FileInput)

    #  class Meta:
    #     model = Articulo
    #     fields = ('categoria', 'nombre', 'marca', 'precio_unitario', 'stock', 'disponible', 'imagen')


class ItemFormulario(forms.Form):
    cantidad = forms.IntegerField()