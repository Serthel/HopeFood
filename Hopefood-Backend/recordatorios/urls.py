from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import recordatorioViewSet

router = DefaultRouter()
router.register(r'', recordatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]