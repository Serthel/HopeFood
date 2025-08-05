# perfil/models.py

from django.db import models
from django.conf import settings

class Perfil(models.Model):
   
   
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, help_text="Una pequeña biografía o descripción del usuario.")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
