from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dashboard funcionando correctamente.")

# Create your views here.
