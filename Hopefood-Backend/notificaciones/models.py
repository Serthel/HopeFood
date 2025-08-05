from django.db import models

class notificacion(models.Model):

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    vista = models.BooleanField(default=False)
    enviada_por_email = models.BooleanField(default=False)  
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
