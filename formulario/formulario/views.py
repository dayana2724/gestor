from django.http import HttpResponse
from django.shortcuts import render 
import datetime

def formulario(request):
    return render(request, "formulario.html")

def respuesta(request):
    nombre=request.GET["nombre"]
    mensaje="hola %r BIENVENIDO" %(nombre)
    return HttpResponse(mensaje)

def respuesta(request):
    agnoActual=datetime.datetime.now().year
    diaActual=datetime.datetime.now().day
    mesActual=datetime.datetime.now().month
    agnoNacimiento= int(request.GET["nacimiento"].split('_')[0])
    mesNacimiento=int(request.GET["nacimiento"].split('_')[1])
    diaNacimiento=int(request.GET["nacimiento"].split('_')[2])
    
    edad=agnoActual - agnoNacimiento
    if mesNacimiento > mesActual:
        edad-=1
    elif mesActual==mesNacimiento:
        if diaActual < diaNacimiento:
            edad-=1
            
            
    nombre=request.GET["nombre"]
    genero=request.GET["genero"]
    return render(request, 'respu.html', {'nombre':nombre, 'edad':edad,'genero':genero})


    

