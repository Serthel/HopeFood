from django.urls import path
from . import views  # Asegúrate de que tienes una vista para enrutar

urlpatterns = [
    # Agrega aquí tus rutas, por ejemplo:
    path('', views.index, name='dashboard-home'),
]
