from django.db import models

class recodatorio(models.Model):

    
    pedido = models.OneToOneField('pedidos.Pedido', on_delete=models.CASCADE)
    minutos_antes = models.IntegerField(default=60)
    enviado = models.BooleanField(default=False)


    def __str__(self):
        return self.pedido
