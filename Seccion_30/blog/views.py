from django.views.generic import DetailView, TemplateView, ListView

from .models import Post

# Tu vista para renderizar el HTML del Blog
class BlogView(DetailView):
    model = Post
    template_name = 'blog.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')    # Status=1 significa que solo se mostrarán las entradas de blog que estén publicadas (status=1).
    template_name = 'index.html'