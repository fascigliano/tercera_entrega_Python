from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=25, default="Python")  #indicar tipo de dato y cantidad de caracteres en este caso. Default es lo que aparece si no le completamos nada.
    camada = models.IntegerField()

class Articulo(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=300)
    contenido =models.CharField(max_length=2000)

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    contraseña =models.CharField(max_length=30)
    profesion = models.CharField(max_length=30, default="Periodista")
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    contraseña =models.CharField(max_length=30)