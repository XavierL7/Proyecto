from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Página principal
    path('', index, name='index'),

    # Apps
    path('posts/', include(('apps.posts.urls', 'posts'), namespace='posts')),
    path('contacto/', include(('apps.contacto.urls', 'contacto'), namespace='contacto')),
    path('usuario/', include(('apps.usuario.urls', 'usuario'), namespace='usuario')),

    # Autenticación
    path('auth/', include('django.contrib.auth.urls')),
]

# Archivos estáticos y media (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()