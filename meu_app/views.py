# meu_app/views.py

from rest_framework import viewsets
from django.shortcuts import render
from .models import Medico, PlanoDeSaude, MedicoAtendePlano
from .serializers import MedicoSerializer, PlanodeSaudeSerializer, MedicoAtendePlanoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PlanoDeSaudeViewSet(viewsets.ModelViewSet):
    queryset = PlanoDeSaude.objects.all()
    serializer_class = PlanodeSaudeSerializer

class MedicoAtendePlanoViewSet(viewsets.ModelViewSet):
    queryset = MedicoAtendePlano.objects.all()
    serializer_class = MedicoAtendePlanoSerializer

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'meu_app/medicos_lista.html', {'medicos': medicos})

def lista_planos(request):
    planos = PlanoDeSaude.objects.all()
    return render(request, 'meu_app/planos_lista.html', {'planos': planos})

def lista_medicos_planos(request):
    medicos_planos = MedicoAtendePlano.objects.all()
    return render(request, 'meu_app/medicos_planos_lista.html', {'medicos_planos': medicos_planos})