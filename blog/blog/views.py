from django.shortcuts import render

def index(request): 
    return render (request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html', {})