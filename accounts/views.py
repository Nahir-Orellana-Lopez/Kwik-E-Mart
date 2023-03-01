from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

def login(request):
    plantilla = loader.get_template("accounts/login.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)

def signup(request):
    plantilla = loader.get_template("accounts/signup.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)