from django.urls import path
from .views import home, registro, login  # Importar las funciones de las vistas
from django.contrib.auth import views as auth_views

# Definir las URL del proyecto
urlpatterns = [
    # URL para la página de inicio
    path('', home, name='home'),

    # URL para la página de registro de usuario
    path('registro/', registro, name='registro'),


]
