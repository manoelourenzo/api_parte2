from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, Plano_de_SaudeViewSet

# Criando um roteador para a API REST
router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)  # Registra o ViewSet de médicos
router.register(r'planos', Plano_de_SaudeViewSet)  # Registra o ViewSet de planos de saúde

# Defina as URLs
urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs geradas automaticamente pelo roteador para a API REST
]
