from django.shortcuts import render
from AppKeepCoding.models import Curso, Profesor
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre = 'SQL', camada = "15847")
    curso.save()
    documentoDeTexto = f"Curso: {curso.nombre}, camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def profesor(self):
    profesor = Profesor(nombre = "Pepe", apellido = "Rodriguez", email = "peperod@upna.com", profesion = "Decano Ingenieria")
    profesor.save()
    documentoDeTexto2 = f"Profesor: {profesor.nombre}, cargo: {profesor.profesion}"
    return HttpResponse(documentoDeTexto2)