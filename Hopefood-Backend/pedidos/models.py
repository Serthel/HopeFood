from django.db import models

class pedido(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),

    )
    
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    email = models.EmailField()
    direccion_entrega = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='pendiente')
    productos = models.ManyToManyField('productos.Producto', related_name='pedidos')

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente}'
