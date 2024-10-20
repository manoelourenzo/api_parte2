# meu_projeto/clinica/models.py
from django.db import models
from django.db.models import UniqueConstraint


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    id_funcionario = models.IntegerField()  
    crm = models.CharField(max_length=20) 
    
    class Meta:
        db_table = 'medico'  
        managed = False  

class PlanoDeSaude(models.Model):
    id_plano = models.AutoField(primary_key=True)
    tipo_cobertura = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)

    class Meta:
        db_table = 'plano_de_saude'
        managed = False

class MedicoAtendePlano(models.Model):
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='id_medico', primary_key=True)
    id_plano = models.ForeignKey(PlanoDeSaude, on_delete=models.CASCADE, db_column='id_plano')

    class Meta:
        db_table = 'medico_atende_plano'
        managed = False  # A tabela já existe no banco
        unique_together = (('id_medico', 'id_plano'),)  # Define chave composta

