from django.urls import path 
from .views import CursoView, DocentesView, index

urlpatterns = [
    path('cursos/', CursoView.as_view(), name='cursos_list'),
    path('docentes/', DocentesView.as_view(), name='docentes_list'),
    path("", index, name="index")
]