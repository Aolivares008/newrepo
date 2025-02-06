from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    html_response = "<h1>Mi Pagina Web web</h1>"
    for i in range (10):
        html_response += "<p>Esto es la portada</p>"
    return HttpResponse (html_response)