from django.shortcuts import render
from rest_framework import viewsets
from .models import Etiqueta
from .serializers import EtiquetaPedidoerializer

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaPedidoerializer
