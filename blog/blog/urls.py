from django.contrib import admin
from django.urls import path, include

from apps.posts.views import PostHomeView
from .views import index, sobre_nosotros
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostHomeView.as_view(), name='index'),                     
    path('posts/', include(('apps.posts.urls', 'apps.posts'), namespace='apps.posts')),
    path('contacto/', include(('apps.contacto.urls', 'apps.contacto'), namespace='apps.contacto')),
    path('usuario/', include(('apps.usuario.urls', 'apps.usuario'), namespace='apps.usuario')),   
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('sobre-nosotros/', sobre_nosotros, name='sobre_nosotros'),
=======
    path("calculadora/", include("apps.calculadora.urls")),
>>>>>>> c7692150c1088b74710fef39356be0e91bb89941
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)