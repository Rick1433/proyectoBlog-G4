from django.contrib import admin
from .models import Post, Categoria

#registro de la clase para ver en el panel admin
admin.site.register(Post)
admin.site.register(Categoria)


