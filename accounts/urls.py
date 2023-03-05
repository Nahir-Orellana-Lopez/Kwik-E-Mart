from django.urls import path
from accounts import views
from django.shortcuts import redirect

# app_name = 'accounts'
urlpatterns = [
    path('', lambda request: redirect('login/', permanent=True)),
    path('login/', views.login_req, name="Login"),
    path('logout/', views.logout_req, name="Logout"),
    path('signup/', views.signup, name="Signup"),
    path('perfil/', views.editarPerfil, name="Perfil"), 
    path('perfil/password/', views.editarPassword, name="PasswordChange"),
    path('clientes/', views.clientes, name="Clientes"),
]