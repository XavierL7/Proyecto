from django.urls import path
from . import views

app_name = "calculadora"

urlpatterns = [
    path("imc/", views.calculadora_imc, name="calculadora_imc"),
]
