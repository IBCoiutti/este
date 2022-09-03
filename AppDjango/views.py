from django.shortcuts import render
from django.http import HttpResponse
from AppDjango.models import Familiar
from django.template import loader, context
# Create your views here.

def familia(request):
    family1= Familiar(nombre="Ignacio", apellido="Rodriguez", dni=38686504, fecha_nacimiento='1995-02-21', residencia="Ricardo Rojas", email="ignacio.ba@hotmail.com")
    family2=Familiar(nombre="Jose", apellido="Lescano", dni=18956458, fecha_nacimiento="1975-06-05", residencia="Ricardo Rojas", email="joselesca756@hotmail.com")
    family3= Familiar(nombre="Arturo", apellido="Rodriguez", dni=40152135, fecha_nacimiento="1998-01-06", residencia="Los Polvorines", email="r2d2rodriguez@outlook.com")
    family1.save()
    family2.save()
    family3.save()
    diccionario={"Nombre":family1.nombre, "Apellido":family1.apellido, "DNI":family1.dni, "Fecha_de_nacimiento":family1.fecha_nacimiento, "Residencia":family1.residencia, "E-mail":family1.email}
    diccionario2={"Nombre":family2.nombre, "Apellido":family2.apellido, "DNI":family2.dni, "Fecha_de_nacimiento":family2.fecha_nacimiento, "Residencia":family2.residencia, "E-mail":family2.email}
    diccionario3={"Nombre":family3.nombre, "Apellido":family3.apellido, "DNI":family3.dni, "Fecha_de_nacimiento":family3.fecha_nacimiento, "Residencia":family3.residencia, "E-mail":family3.email}
    return render(request, 'template.html', context={"dic":diccionario, "dic2":diccionario2, "dic3":diccionario3})






