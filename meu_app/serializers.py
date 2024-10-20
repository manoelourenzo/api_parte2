# meu_app/serializers.py

from rest_framework import serializers
from .models import Medico, PlanoDeSaude, MedicoAtendePlano

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'  # Isso inclui todos os campos do modelo

class PlanodeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoDeSaude
        fields = '__all__'  # Isso inclui todos os campos do modelo

class MedicoAtendePlanoSerializer(serializers.ModelSerializer): 
    id_medico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all()) 
    id_plano = serializers.PrimaryKeyRelatedField(queryset=PlanoDeSaude.objects.all())

    class Meta:
        model = MedicoAtendePlano
        fields = '__all__'