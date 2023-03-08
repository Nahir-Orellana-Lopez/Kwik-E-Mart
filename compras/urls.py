from django.urls import path
from compras import views

# app_name = 'compras'
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('articulos/', views.articulos, name="Articulos"),
    path('articulos/<articulo_id>', views.verArticulo, name="VerArticulo"),
    path('articulos/agregar/', views.agregarArticulo, name="AgregarArticulo"),
    path('articulos/editar/<articulo_id>', views.editarArticulo, name="EditarArticulo"),
    path('articulos/eliminar/<articulo_id>', views.eliminarArticulo, name="EliminarArticulo"),
    path('articulos/valorar/<articulo_id>', views.valorarArticulo, name="ValorarArticulo"),
    path('carrito/', views.carrito, name="Carrito"),
    path('carrito/<cliente_id>', views.carrito, name="Carrito"),
    path('carrito/eliminar/<item_id>', views.eliminarItem, name="EliminarItem"),
    path('carrito/agregar/<articulo_id>', views.agregarItem, name="AgregarItem"),
    path('carrito/set/<item_id>', views.setItem, name="SetItem"),
    path('acercaDeMi/', views.acercaDeMi, name="AcercaDeMi"),
] 
