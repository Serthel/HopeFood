from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import notificacionViewSet

router = DefaultRouter()
router.register(r'', notificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]