from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ComentarioForm, CrearPostForm, NuevaCategoriaForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Categoria, Post, Comentario
from django.views.generic.edit import CreateView 
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect 
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/posts_individuales.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:posts_individuales', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response (context)
        
               
        
class PostCreateView(CreateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'posts/crear_post.html'
    success_url = reverse_lazy('apps.posts:posts')
    

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/crear_categoria.html'
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.posts:post_create')    
                
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = 'comentario/comentarios/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['posts_id']
        return super().form_valid(form)        
    
    