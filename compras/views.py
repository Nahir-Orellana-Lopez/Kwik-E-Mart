from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from compras.forms import ArticuloFormulario, ItemFormulario
from accounts.models import Avatar
from .models import Articulo, ItemCarrito
from ast import literal_eval

def inicio(request):
    plantilla = loader.get_template("compras/inicio.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    avatar = ""
    if(len(avatares) >= 1):
        avatar = avatares[0].imagen.name
    documento = plantilla.render({"avatar": avatar},request)
    return HttpResponse(documento)

def articulos(request):
    categorias = request.GET.get('categorias', '')
    nombre = request.GET.get('nombre', '')
    marca = request.GET.get('marca', '')
    articulos = Articulo.objects.filter(categorias__icontains=categorias,
                                        nombre__icontains=nombre,
                                        marca__icontains=marca).order_by('nombre')
    contexto = {"articulos": articulos,"categoria":categorias, "nombre":nombre, "marca":marca}
    plantilla = loader.get_template("compras/articulos.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
@staff_member_required
def agregarArticulo(request):
    form = ArticuloFormulario()
    if request.method == 'POST':
        form = ArticuloFormulario(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            articulo = Articulo(nombre=informacion['nombre'],  
                            categorias=informacion['categorias'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"],
                            imagen=informacion["imagen"])
            articulo.save()
            return HttpResponseRedirect("/compras/articulos")
             
    contexto = {"form": form}
    plantilla = loader.get_template("compras/agregarArticulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
@staff_member_required
def editarArticulo(request, articulo_id):
    form = ArticuloFormulario()
    if request.method == 'POST':
        form = ArticuloFormulario(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            articulo = Articulo(id=articulo_id,
                            nombre=informacion['nombre'],  
                            categorias=informacion['categorias'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"],
                            imagen=informacion["imagen"])
            fields_to_exclude = {}
            if(articulo.imagen == None):
                fields_to_exclude = {'imagen'}
            fields_to_update = [f.name for f in articulo._meta.get_fields() if f.name not in fields_to_exclude and not f.auto_created]
            articulo.save(update_fields=fields_to_update)
            return HttpResponseRedirect("/compras/articulos/"+articulo_id)
             
    articulo = Articulo.objects.get(id=articulo_id)
    categorias = literal_eval(articulo.categorias)
    form = ArticuloFormulario(initial={"nombre":articulo.nombre, 
                                               "categorias": categorias, 
                                               "marca": articulo.marca,
                                               "precio_unitario": articulo.precio_unitario,
                                               "stock": articulo.stock,
                                               "disponible": articulo.disponible,
                                               "imagen": articulo.imagen
    })
    contexto = {"articulo": articulo, "form": form}
    plantilla = loader.get_template("compras/editarArticulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
@staff_member_required
def eliminarArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    articulo.delete()
    return HttpResponseRedirect('/compras/articulos')

def verArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    contexto = {"articulo": articulo}
    plantilla = loader.get_template("compras/articulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)


@login_required
def carrito(request):     
    cliente = request.user
    carrito = ItemCarrito.objects.all().filter(cliente_id=cliente.id)
    for i in carrito:
        i.suma_parcial = i.articulo.precio_unitario * i.cantidad
    contexto = {"carrito": carrito}
    plantilla = loader.get_template("compras/carrito.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def eliminarItem(request, item_id):
    item = ItemCarrito.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/compras/carrito/')

@login_required
def agregarItem(request, articulo_id):
    cliente = request.user
    cantidad = request.POST.get('cantidad', 0)
    if(int(cantidad)>0):
        item = ItemCarrito(cantidad=cantidad,
                            articulo=Articulo(id=articulo_id),
                            cliente=cliente)
        item.save()
    return HttpResponseRedirect('/compras/carrito/')

def acercaDeMi(request):
    plantilla = loader.get_template("compras/acercaDeMi.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)
