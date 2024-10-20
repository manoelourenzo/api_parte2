from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet  

# Criando um roteador para a API REST
router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)  # Registra o ViewSet de médicos

# Defina as URLs
urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs geradas automaticamente pelo roteador para a API REST
]
