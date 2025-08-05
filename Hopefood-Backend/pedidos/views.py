from django.shortcuts import render
from rest_framework import viewsets
from .models import pedido
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer

