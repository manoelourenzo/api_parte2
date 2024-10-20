# meu_app/views.py

from rest_framework import viewsets
from django.shortcuts import render
from .models import Medico, Plano_de_Saude
from .serializers import MedicoSerializer, Plano_de_SaudeSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class Plano_de_SaudeViewSet(viewsets.ModelViewSet):
    queryset = Plano_de_Saude.objects.all()
    serializer_class = Plano_de_SaudeSerializer

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'meu_app/medicos_lista.html', {'medicos': medicos})

def lista_planos(request):
    planos = Plano_de_Saude.objects.all()
    return render(request, 'meu_app/planos_lista.html', {'planos': planos})