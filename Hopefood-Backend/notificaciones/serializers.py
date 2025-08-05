from rest_framework import serializers
from .models import notificacion

class notificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificacion
        fields = '__all__'