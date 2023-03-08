## Proyecto Final de Coderhouse - Nahir Orellana Lopez 

El proyecto se trata de una página web que simula una tienda online del conocido minimercado de los Simpsons, el Kwik-E-Mart. Cuenta con usuarios admin y clientes. Los admin pueden agregar, editar y eliminar artículos. Los clientes pueden agregar artículos a sus carritos de compra y valorarlos.

### Acerca de mí
Mi nombre es Nahir Orellana Lopez, soy profesora de matemática y estudiante de la tecnicatura universitaria en desarrollo web. 

### Tecnologías
Python - SQLite - Django - HTML - Bootstrap

# Kwik-E-Mart Online

## Pantalla de Inicio
<img src="https://user-images.githubusercontent.com/124831483/223578483-047dbacd-8810-4e80-97b7-9c6269c9fef6.png" width=600px>

### Navegación
- _Inicio_: Lleva a la página de inicio
- _Artículos_: Ver lista y funcionalidades de todos los artículos
- (Sólo Admin)
  - _Clientes_: Ver lista y funcionalidades de todos los clientes
- (Sólo Cliente)
  - _Carrito_: Ver items del carrito de compras
- _Acerca de_: Ver información del dueño de la tienda virtual
- _Login_: Lleva a la página de login de usuarios
- _Registro_: Lleva a la página de registro de usuarios

## Login como Admin
<img src="https://user-images.githubusercontent.com/124831483/223580540-e9765f1a-7c69-4254-8bb4-cd2ae82bf392.png" width=400px>

- Usuario: apu
- Contraseña: contraseña

### Funcionalidades
#### Ver Artículos
<img src="https://user-images.githubusercontent.com/124831483/223580935-9d7b20ac-9d10-4dca-a6be-f90b2f08379c.png" width=600px>

- [Buscar]: Busca artículos por los criterios de nombre, marca y categoría
- [Limpiar]: Limpia el filtro de búsqueda
- [Ver]: Dirige al detalle del artículo
- [Eliminar]: Elimina el artículo
- [Agregar]: (Botón al final de la página) Lleva al formulario de creación de un nuevo artículo

#### Agregar Artículo
<img src="https://user-images.githubusercontent.com/124831483/223583634-849da785-87b8-4078-b4f1-4149ee89b2c3.png" width=400px>

- [Guardar]: Guarda el artículo y redirige a la lista de artículos

#### Ver Detalle de Artículo
<img src="https://user-images.githubusercontent.com/124831483/223582912-5baeb70d-89b5-42b9-bd5c-413a5fee0c80.png" width=650px>

- [Editar]: Lleva a la página de edición del artículo (Similar a [Agregar])
- [Eliminar]: Elimina el artículo
- [Volver]: Vuelve a la lista de artículos

#### Ver Clientes
<img src="https://user-images.githubusercontent.com/124831483/223581976-33374a38-7360-404a-80a1-1eab71825446.png" width=600px>

- [Ver]: Muestra los items del carrito del cliente seleccionado, sin las funcionalidades de agregar o eliminar

## Registro de Cliente
<img src="https://user-images.githubusercontent.com/124831483/223588541-30c98051-21d7-4546-87a3-81e893b052b3.png" width=400px>

## Login como Cliente
- Usuario: homero
- Contraseña: contraseña

### Funcionalidades
#### Ver Artículos
<img src="https://user-images.githubusercontent.com/124831483/223591040-cd74e5a7-8434-4158-8c41-30217b45c4a2.png" width=750px>

- [Ver]: Dirige al detalle del artículo
- [Agregar]: Agrega un ítem al carrito de compras con la cantidad especificada

#### Ver/Valorar Artículo
<img src="https://user-images.githubusercontent.com/124831483/223618373-e24e0892-2fa3-4251-b57e-8a88e937e109.png" width=800px>

- [Enviar]: Envía la valoración del artículo y la agrega a la lista

#### Ver Carrito
<img src="https://user-images.githubusercontent.com/124831483/223589696-95d15de2-57a6-4fcf-a08f-4b7cb630a1ef.png" width=700px>

- [Cambiar]: Cambia la cantidad del ítem, teniendo como máximo el stock del artículo. Al hacerlo se actualizan los costos
- [Eliminar]: Elimina el ítem del carrito
- [Seguir Comprando]: Dirige a la lista de artículos

#### Mi Perfil
<img src="https://user-images.githubusercontent.com/124831483/223591622-00591e5a-54df-4ea9-9d11-a6c4c0d17564.png" width=400px>

- [Cambiar Contraseña]: Dirige a la página de cambio de contraseña
- [Guardar]: Guarda los cambios del usuario
