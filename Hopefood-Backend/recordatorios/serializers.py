from rest_framework import serializers
from .models import recordatorio

class recordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = recordatorio
        fields = '__all__'