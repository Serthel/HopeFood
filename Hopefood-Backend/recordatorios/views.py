from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import recordatorio
from .serializers import recordatorioSerializer

class recordatorioViewSet(viewsets.ModelViewSet):
    queryset = recordatorio.objects.all()
    serializer_class = recordatorioSerializer