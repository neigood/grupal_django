from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("HOLA somos telovendo equipo 2 dejando nuestra marca")