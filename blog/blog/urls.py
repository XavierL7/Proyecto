from django.contrib import admin
from django.urls import path, include

from apps.posts.views import PostHomeView
from .views import index
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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)