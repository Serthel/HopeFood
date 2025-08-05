from rest_framework import serializers
from .models import pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'
