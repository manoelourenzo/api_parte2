# meu_projeto/clinica/models.py
from django.db import models

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    id_funcionario = models.IntegerField()  
    crm = models.CharField(max_length=20) 
    
    class Meta:
        db_table = 'medico'  
        managed = False  

class Plano_de_Saude(models.Model):
    id_plano = models.AutoField(primary_key=True)
    tipo_cobertura = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)

    class Meta:
        db_table = 'plano_de_saude'
        managed = False