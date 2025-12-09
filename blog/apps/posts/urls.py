
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, CategoriaCreateView
from . import views

app_name = "apps.posts"
urlpatterns = [
    path ('posts/' , PostListView.as_view(), name='posts'),
    path ('posts/<int:id>/' , PostDetailView.as_view(), name='posts_individuales'),
    path ('post/' , PostCreateView.as_view(), name='crear_post'),
    path ('posts/categoria' , CategoriaCreateView.as_view(), name='crear_categoria'),
]
