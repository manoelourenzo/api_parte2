# meu_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, PlanoDeSaudeViewSet, MedicoAtendePlanoViewSet, delete_medico_plano

# Criando um roteador para a API REST
router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)  
router.register(r'planos', PlanoDeSaudeViewSet) 
router.register(r'medicos-planos', MedicoAtendePlanoViewSet, basename='medicoatendeplano') 


urlpatterns = [
    path('', include(router.urls)), 
    path('medicos-planos/<int:id_medico>/<int:id_plano>/', delete_medico_plano, name='delete_medico_plano'), # DELETE
]