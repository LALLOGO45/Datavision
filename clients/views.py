# Create your views here.
# clients/views.py
from django.shortcuts import render
from .models import Client, Projet

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste_clients.html', {'clients': clients})

def detail_client(request, id):
    client = Client.objects.get(id=id)
    projets = Projet.objects.filter(client=client)
    return render(request, 'clients/detail_client.html', {'client': client, 'projets': projets})
