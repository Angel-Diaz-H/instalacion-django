
from django.contrib import admin
from django.urls import path
from usuarios.views import MostrarCorreos,MostrarHtmlView

urlpatterns = [
    path("mostrar/",MostrarCorreos.as_view()),
    path("holamundo/",MostrarHtmlView.as_view()),
]
