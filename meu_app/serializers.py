# meu_app/serializers.py

from rest_framework import serializers
from .models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'  # Isso inclui todos os campos do modelo
