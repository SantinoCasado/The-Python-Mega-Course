from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')  # Muestra los campos title, author, status y created_at en la lista de entradas de blog en el panel de administración.
    list_filter = ('status', 'created_at')  # Permite filtrar las entradas de blog por estado (borrador o publicado) y por fecha de creación en el panel de administración.
    search_fields = ('title', 'content')  # Permite buscar entradas de blog por título y contenido en el panel de administración.
    prepopulated_fields = {'slug': ('title',)}  # Genera automáticamente el campo slug a partir del título de la entrada de blog en el panel de administración.


admin.site.register(Post, PostAdmin) # Registra el modelo Post en el panel de administración de Django, lo que permite a los administradores del sitio web crear, editar y eliminar entradas de blog a través de la interfaz de administración.