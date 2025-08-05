from rest_framework import serializers
from .models import EstadoPedido

class EstadoPedidoerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'