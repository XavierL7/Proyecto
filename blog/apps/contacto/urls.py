from django.urls import path
from .views import ContactoUsuario

app_name = "contacto"

urlpatterns = [
    path('', ContactoUsuario.as_view(), name='contacto'),
]
