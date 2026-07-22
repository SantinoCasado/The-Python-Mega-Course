from . import views
from django.urls import path

urlpatterns = [
    path('', views.Translator_view, name='translator_view'),  # Ruta para ver el home en tu navegador (usa la clase de tu frontend)
]