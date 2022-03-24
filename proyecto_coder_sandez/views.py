from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def primer_vista(request):
    return HttpResponse("Hola mundo uno dos tres probando...")

def segunda_vista(request):
    return HttpResponse("<h1>Titulo 1</h1> <p>Esto es un parrafo </p>")

def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"<p>Tiempo actual: {fecha_hora}</p>")

def nombre_usuario(request, nombre):
    return HttpResponse(f"Tu nombre es {nombre}")

def edad_usuario(request, edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse(f"Ud nacio el {anio_nacimiento}")

# def pagina_inicio(request):
#     archivo = open(r"C:\Users\Cocardo\Documents\django-intro\proyecto_coder_sandez\proyecto_coder_sandez\templates\page.html", 'r')

#     nombre = "Juan"
#     apellido = "Sandez"
#     fecha_hora = datetime.now()

#     listado_calificaciones = [10,9,6]
# #Diccionario con los datos que enviaremos como Contexto
#     dict_context = {"nombre": nombre, "apellido":apellido, "fecha_hora": fecha_hora,"listado": listado_calificaciones}

#     plantilla = Template(archivo.read())

#     archivo.close()



#     context = Context(dict_context)

#     documento = plantilla.render(context)

#     return HttpResponse(documento)


def pagina_inicio(request):

    nombre = "Juan"
    apellido = "Sandez"
    fecha_hora = datetime.now()

    listado_calificaciones = [10,9,6]
   # Diccionario con los datos que enviaremos como Contexto
    dict_context = {"nombre": nombre, "apellido":apellido, "fecha_hora": fecha_hora,"listado": listado_calificaciones}
    
    plantilla = loader.get_template("page.html")

    documento = plantilla.render(dict_context)

    return HttpResponse(documento)    


