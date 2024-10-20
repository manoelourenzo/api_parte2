#urls.py de meu_projeto

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meu_app.urls')),  # Inclua o URLs do seu aplicativo
]
