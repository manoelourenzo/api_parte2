# meu_projeto/clinica/models.py
from django.db import models

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    id_funcionario = models.IntegerField()  
    crm = models.CharField(max_length=20) 
    
    class Meta:
        db_table = 'medico'  
        managed = False  
