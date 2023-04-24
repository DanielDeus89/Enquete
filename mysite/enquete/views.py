from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá, este é o meu primeiro projeto Django!</h1>")
