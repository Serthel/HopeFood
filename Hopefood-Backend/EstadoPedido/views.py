from django.shortcuts import render
from rest_framework import viewsets
from .models import EstadoPedido
from .serializers import EstadoPedidoerializer

class EstadoPedidoviewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoerializer