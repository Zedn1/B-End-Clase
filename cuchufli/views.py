from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pag1(request):
    html = """
    <h1>C U<h1>
    <h2>C H U<h2>
    <h3>F L I<h3>
    """
    return HttpResponse(html)

def pag2(request):
    page = """
    <h1>Solo soy la página de testeo 2<h1>
    """
    return HttpResponse(page)
