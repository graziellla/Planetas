from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

def listarPlanetas(request):
    planeta = Planeta.objects.all()

    contexto = {
        "todos_planetas": planeta
    }
    return render(request,'listar.html',contexto)
# Create your views here.

def umPlaneta(request, idplaneta=None):
    planeta = Planeta.objects.get(id=idplaneta)
    contexto = {
        "planeta": planeta,
    }
    return render(request, 'planeta.html', contexto)

