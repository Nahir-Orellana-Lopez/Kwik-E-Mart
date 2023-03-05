from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserRegisterForm, UserEditForm
from accounts.models import Avatar

@login_required
def logout_req(request):
    logout(request)
    url = reverse('Inicio')
    return HttpResponseRedirect(url)

def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                url = reverse('Inicio')
                return HttpResponseRedirect(url)
            else:
                return render(request, "accounts/login.html", {"form": form, "error":"No se puede autenticar el usuario"})
        else:
            return render(request, "accounts/login.html", {"form": form, "error":"Los datos son incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            avatar = Avatar(user=form.id, imagen=form.cleaned_data["avatar_img"])
            avatar.save()
            url = reverse('Login')
            return HttpResponseRedirect(url)
    else:
        form = UserRegisterForm()     
    return render(request,"accounts/signup.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            informacion = form.cleaned_data
            nuevo_avatar = informacion["avatar_img"]
            if(nuevo_avatar):
                avatares = Avatar.objects.filter(user=usuario.id)
                if(len(avatares) >= 1):
                    avatar = avatares[0]
                    avatar.imagen = informacion["avatar_img"]
                    avatar.save()
                else:
                    avatar = Avatar(user=usuario, imagen=informacion["avatar_img"])
                    avatar.save()
            form.save()
            url = reverse('Inicio')
            return HttpResponseRedirect(url)
    else:
        avatares = Avatar.objects.filter(user=usuario.id)
        avatar = ""
        if(len(avatares) >= 1):
            avatar = avatares[0]
            avatar_filename = avatar.imagen.name
        form = UserEditForm(initial={'email': usuario.email, 
                                             'first_name': usuario.first_name, 
                                             'last_name': usuario.last_name,
                                             'username': usuario.username,
                                             'avatar_img': avatar_filename})
    return render(request, "accounts/editarPerfil.html", {"form": form, "usuario": usuario})

@login_required
def editarPassword(request):
    usuario = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(usuario, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            url = reverse('Login')
            return HttpResponseRedirect(url)
        else:
            return render(request, "accounts/editarPassword.html", {"form": form, "error":"Los datos son incorrectos"})
    else:
        form = PasswordChangeForm(usuario)
    return render(request, "accounts/editarPassword.html", {"form": form, "usuario": usuario})

@login_required
@staff_member_required
def clientes(request):  
    clientes = User.objects.filter(is_staff=False)
    for c in clientes:
        avatares = Avatar.objects.filter(user=c.id)
        if(len(avatares) >= 1):
            avatar = avatares[0]           
            c.imagen = avatar.imagen.name
    contexto = {"clientes": clientes}
    plantilla = loader.get_template("accounts/clientes.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)