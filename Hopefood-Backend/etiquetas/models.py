from django.db import models
import uuid

class Etiqueta(models.Model):

        pedido = models.ForeignKey('pedidos.pedido', on_delete=models.CASCADE, related_name='etiquetas')
        numero_orden = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
        fecha_entrega = models.DateField()
        codigo_rastreo = models.CharField(max_length=100, unique=True, null=True, blank=True)
        qr = models.ImageField(upload_to='etiquetas/', blank=True, null=True)

        
        def __str__(self):
            return self.pedido

