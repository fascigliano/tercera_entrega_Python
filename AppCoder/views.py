from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader
from .models import Curso
from django.shortcuts import render


def inicio(request):
	plantilla = loader.get_template('index.html')
	docu = plantilla.render()
	return HttpResponse(docu)

def curso(request, nombre, numero):
	curso = Curso(nombre=nombre, camada= int(numero))
	curso.save()
	documento=f"curso:{curso.nombre}<br> Camada:{curso.camada}"
	return HttpResponse(documento)
def IniciaSesion(request):
	plantilla = loader.get_template('IniciaSesion.html')
	docu = plantilla.render()
	return HttpResponse(docu)
def Nosotros(request):
	plantilla = loader.get_template('Nosotros.html')
	docu = plantilla.render()
	return HttpResponse(docu)
def CrearCuenta(request):
	plantilla = loader.get_template('CrearCuenta.html')
	docu = plantilla.render()
	return HttpResponse(docu)
def Articulos(request):
	plantilla = loader.get_template('Articulos.html')
	docu = plantilla.render()
	return HttpResponse(docu)