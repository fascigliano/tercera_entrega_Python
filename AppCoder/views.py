from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from AppCoder.models import *

def inicio(request):
    return render(request, 'index.html')
def IniciaSesion(request):
	return render(request, "IniciaSesion.html")
def Nosotros(request):
	return render(request, "Nosotros.html")
def CrearCuenta(request):
    if request.method == 'POST':
        usuario = Usuario(nombre=request.POST['nombre'], apellido=request.POST['apellido'], usuario=request.POST['usuario'], contraseña=request.POST['contraseña'])
        usuario.save()
    return render(request, "CrearCuenta.html")

def Articulos(request):
	return render(request, 'Articulos.html')
def Escribir(request):
    if request.method == 'POST':
        articulo = Articulo(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], contenido=request.POST['articulo'])
        articulo.save()
    return render(request,'Escribir.html')

def Ser_Escritor(request):
    if request.method == 'POST':
        usuario = Autor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], usuario=request.POST['usuario'], contraseña=request.POST['contraseña'], profesion=request.POST['profesion'])
        usuario.save()
    return render(request, "Ser_Escritor.html")

def Buscar_Articulos(request):
    return render(request,"BuscarArticulos.html")

