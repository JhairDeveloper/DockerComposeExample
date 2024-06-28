from typing import Any
from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from .models import Curso, Docentes
from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        docentes = list(Docentes.objects.values())
        if(len(docentes)):
            datos = {'message': 'Success', 'docentes': docentes}
        else:
            datos = {'message': 'Docentes no encontrados...'}
        return JsonResponse(datos)
    
    def post(self, request):
        # print(request.body)
        datos = {'message': 'Successsss'}
        return JsonResponse(datos)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")