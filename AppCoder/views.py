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

    return render(request, "CrearCuenta.html")

def Articulos(request):
	return render(request, 'Articulos.html')
