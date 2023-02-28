from django.urls import path
from compras import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.clientes, name="Clientes"),
    path('eliminarCliente/<cliente_id>', views.eliminarCliente, name="EliminarCliente"),
    path('articulos/', views.articulos, name="Articulos"),
    path('eliminarArticulo/<articulo_id>', views.eliminarArticulo, name="EliminarArticulo"),
    path('carrito/<cliente_id>', views.carrito, name="Carrito"),
    path('eliminarItem/<item_id>/<cliente_id>', views.eliminarItem, name="EliminarItem"),
    path('agregarItem/<articulo_id>/<cliente_id>', views.agregarItem, name="AgregarItem"),
    path('buscarArticulos/<cliente_id>/', views.buscarArticulos, name="BuscarArticulos"),
    path('acercaDeMi/', views.acercaDeMi, name="AcercaDeMi"),
]
