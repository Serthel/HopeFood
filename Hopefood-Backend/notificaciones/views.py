from django.shortcuts import render
from rest_framework import viewsets
from .models import notificacion
from .serializers import notificacionSerializer

class notificacionViewSet(viewsets.ModelViewSet):
    queryset = notificacion.objects.all()
    serializer_class = notificacionSerializer
