from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    # Listado y detalle
    path('', PostListView.as_view(), name='posts'),
    path('<int:id>/', PostDetailView.as_view(), name='posts_individuales'),

    # CRUD de posts
    path('crear/', PostCreateView.as_view(), name='crear_post'),
    path('<int:pk>/modificar/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),

    # Categorías
    path('categoria/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categoria/<int:pk>/post/', PostsPorCategoriaView.as_view(), name='posts_por_categoria'),

    # Comentarios
    path('comentario/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='comentario_editar'),
    path('comentario/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='comentario_delete'),
]