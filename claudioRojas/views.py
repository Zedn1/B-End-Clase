from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexZed(request):
    html="""
    <h1>Titulo de parte del index Zed</h1>
    <h2>Hola Mundo!</h2>
    """
    return HttpResponse(html)

def Zed(request):
    html="""
    <h1>Titulo de Zed</h1>
    <h2>Adios Mundo!</h2>
    """
    return HttpResponse(html)