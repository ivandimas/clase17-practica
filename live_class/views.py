from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context
from django.template import loader


from django.contrib import admin
from django.urls import path
def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> {edad}"


      return HttpResponse(documentoDeTexto)


def probandoTemplate(self):

    miHtml = open("C:/Users\i_dim\OneDrive\Escritorio\PythonProyecto1\live_class\live_class\templates\template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    render = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse (render)
