from django import forms
from .models import Articulo

# class ClienteFormulario(forms.Form):
#     nombre = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     habilitado = forms.BooleanField(initial=True, required=False)

opcionesCategoria = (
    ('bebidas','Bebidas'),
    ('embutidos', 'Embutidos'),
    ('juegos','Juegos'),
    ('juguetes','Juguetes'),
    ('almacen','Almacén'),
    ('golosinas','Golosinas'),
    ('limpieza','Limpieza'),
    ('congelados','Congelados'),
    ('desayuno','Desayuno'),
    ('panaderia','Panadería'),
    ('tabaco','Tabaco'),
    ('revistas','Revistas'),
    ('deportes','Deportes'),
    ('otro', 'Otro'),
    )

class ArticuloFormulario(forms.Form):
    categorias = forms.MultipleChoiceField(label='Categorías', widget=forms.CheckboxSelectMultiple, choices=opcionesCategoria)
    nombre = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    marca = forms.CharField(max_length=20, label='Marca', widget=forms.TextInput(attrs={'class':'form-control'}))
    precio_unitario = forms.FloatField(label='Precio Unitario', widget=forms.NumberInput())
    stock = forms.IntegerField(label='Stock', widget=forms.NumberInput())
    disponible = forms.BooleanField(initial=True, required=False, label='Disponible', widget=forms.CheckboxInput())
    imagen = forms.ImageField(required=False, label='Imagen', widget=forms.FileInput())

    class Meta:
       model = Articulo
       fields = ('categorias', 'nombre', 'marca', 'precio_unitario', 'stock', 'disponible', 'imagen')
    
class ItemFormulario(forms.Form):
    cantidad = forms.IntegerField()