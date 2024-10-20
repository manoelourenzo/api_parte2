# meu_app/views.py

from rest_framework import viewsets
from django.shortcuts import render
from .models import Medico
from .serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'meu_app/medicos_lista.html', {'medicos': medicos})