from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstadoPedidoviewSet

router = DefaultRouter()
router.register(r'', EstadoPedidoviewSet)

urlpatterns = [
    path('', include(router.urls)),
]