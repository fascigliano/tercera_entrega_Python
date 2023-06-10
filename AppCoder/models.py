from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=300)
    contenido =models.CharField(max_length=2000)
    def __str__(self):
        return f"Titulo = {self.titulo} - Subtitulo = {self.subtitulo}"

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    contraseña =models.CharField(max_length=30)
    profesion = models.CharField(max_length=40)
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido =models.CharField(max_length=20)
    usuario = models.CharField(max_length=30)
    contraseña =models.CharField(max_length=30)