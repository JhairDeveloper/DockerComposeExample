from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from .models import Curso, Docentes
from django.http import HttpResponse

# Create your views here.
class CursoView(View):

    def get(self, request):
        cursos = list(Curso.objects.values())
        if(len(cursos)):
            datos = {'message': 'Success', 'cursos': cursos}
        else:
            datos = {'message': 'Cursos no encontrados...'}
        return JsonResponse(datos)

class DocentesView(View):

    def get(self, request):
        docentes = list(Docentes.objects.values())
        if(len(docentes)):
            datos = {'message': 'Success', 'docentes': docentes}
        else:
            datos = {'message': 'Cursos no encontrados...'}
        return JsonResponse(datos)
    
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")