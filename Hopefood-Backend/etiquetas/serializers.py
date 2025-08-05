from rest_framework import serializers
from .models import Etiqueta

class EtiquetaPedidoerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'