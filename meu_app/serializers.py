# meu_app/serializers.py

from rest_framework import serializers
from .models import Medico, Plano_de_Saude

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'  # Isso inclui todos os campos do modelo

class Plano_de_SaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano_de_Saude
        fields = '__all__'  # Isso inclui todos os campos do modelo

