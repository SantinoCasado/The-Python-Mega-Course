from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Clase Post que permite crear entradas de blog con título, contenido y fechas de creación y actualización.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=200)    # Slug es un campo de texto que se utiliza para crear URLs amigables y legibles para los motores de búsqueda. Se utiliza para identificar de manera única una entrada de blog en la URL.
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # author es una relación de clave foránea con el modelo User de Django, lo que significa que cada entrada de blog está asociada a un usuario específico. Si el usuario se elimina, todas sus entradas de blog también se eliminarán automáticamente gracias a on_delete=models.CASCADE.
    status = models.IntegerField(choices=STATUS, default=0)  # status es un campo de tipo IntegerField que utiliza la tupla STATUS para definir los posibles estados de una entrada de blog (borrador o publicado). El valor predeterminado es 0 (borrador).

    def __str__(self):
        return self.title

