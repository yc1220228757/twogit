from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,this world!")


def register(request):
    return HttpResponse("Yeal !")
# Create your views here.
