from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',       # Nombre de tu base de datos
        'USER': 'root',         # Usuario de MySQL
        'PASSWORD': 'root',     # Contraseña de MySQL
        'HOST': 'localhost',    # Servidor MySQL
        'PORT': '3306',         # Puerto por defecto
    }
}