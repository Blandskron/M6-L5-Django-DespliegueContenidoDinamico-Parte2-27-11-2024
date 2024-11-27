from django.shortcuts import render
from .models import Cursos

# Create your views here.
def lista_cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})
