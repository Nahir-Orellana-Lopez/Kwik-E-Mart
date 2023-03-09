from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from compras.forms import ArticuloFormulario, ItemFormulario, MensajeFormulario
from accounts.models import Avatar
from .models import Articulo, ItemCarrito, Mensaje
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
    button = request.GET.get('button', '')
    categorias = ''
    nombre = ''
    marca = ''
    if button == 'Buscar':
        categorias = request.GET.get('categorias', '')
        nombre = request.GET.get('nombre', '')
        marca = request.GET.get('marca', '')
    articulos = Articulo.objects.filter(categorias__icontains=categorias,
                                        nombre__icontains=nombre,
                                        marca__icontains=marca).order_by('nombre')
    if(not request.user.is_staff):
        articulos = articulos.filter(disponible=True)
    for a in articulos:
        a.categorias = literal_eval(a.categorias)
    contexto = {"articulos": articulos,"categorias":categorias, "nombre":nombre, "marca":marca}
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
    try:
        articulo = Articulo.objects.get(id=articulo_id)
    except Articulo.DoesNotExist:
        return HttpResponseRedirect("/compras/articulos")
    articulo.categorias = literal_eval(articulo.categorias)
    valoraciones = Mensaje.objects.filter(articulo=articulo_id)
    valoraciones_cliente = valoraciones.filter(cliente=request.user.id)
    ya_valorado = False
    if(len(valoraciones_cliente)!=0):
        ya_valorado = True
    form = MensajeFormulario()
    contexto = {"articulo": articulo, "form": form, "ya_valorado": ya_valorado, "valoraciones": valoraciones}
    plantilla = loader.get_template("compras/articulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def valorarArticulo(request, articulo_id):
    form = MensajeFormulario()
    if request.method == 'POST':
        form = MensajeFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            mensaje = Mensaje(
                            cliente=request.user,
                            articulo = Articulo(id=articulo_id),
                            mensaje=informacion['mensaje'],  
                            imagen=informacion["escala_img"])
            mensaje.save()
            return HttpResponseRedirect("/compras/articulos/"+articulo_id)

@login_required
def carrito(request, cliente_id=None):
    total = 0
    if not cliente_id:
        usuario = request.user
    else:
        usuario = User.objects.get(id=cliente_id)
        if not request.user.is_staff:
            return HttpResponseRedirect('/compras')
    carrito = ItemCarrito.objects.all().filter(cliente_id=usuario.id)
    for i in carrito:
        i.suma_parcial = i.articulo.precio_unitario * i.cantidad
        total += i.suma_parcial
    contexto = {"carrito": carrito, "total": total, "usuario":usuario}
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
        items = ItemCarrito.objects.filter(articulo=articulo_id, cliente=cliente.id)
        if(len(items)==0):        
            item = ItemCarrito(cantidad=cantidad,
                                articulo=Articulo(id=articulo_id),
                                cliente=cliente)
        else:
            item = items[0]
            if(item.cantidad+int(cantidad)<=item.articulo.stock):
                item.cantidad+=int(cantidad)
            else:
                item.cantidad = item.articulo.stock
        item.save()
    return HttpResponseRedirect('/compras/carrito/')

@login_required
def setItem(request, item_id):
    cantidad = request.POST.get('cantidad', 0)
    if(int(cantidad)>0):
        item = ItemCarrito.objects.get(id=item_id)
        if(int(cantidad)<=item.articulo.stock):
            item.cantidad = int(cantidad)
        else:
            item.cantidad = item.articulo.stock
        item.save()
    return HttpResponseRedirect('/compras/carrito/#'+item_id)

def acercaDeMi(request):
    plantilla = loader.get_template("compras/acercaDeMi.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)
