"""
URL configuration for CursoCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
path('admin/', admin.site.urls),
path("", views.inicio, name="inicio"),
path("Nosotros", views.Nosotros, name="Nosotros"),
path('Inicia_Sesion/', views.IniciaSesion, name="Inicia_Sesion"),
path('Crear_Cuenta/', views.CrearCuenta, name="Crear_Cuenta"),
path('Articulos/', views.Articulos, name="Articulos"),
path('Escribir/', views.Escribir, name="Escribir"),
path('Ser_Escritor/', views.Ser_Escritor, name="Ser_Escritor"),
path('Buscar_Articulos/', views.Buscar_Articulos, name="Buscar_Articulos")
]
