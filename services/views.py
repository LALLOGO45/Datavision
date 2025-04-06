
# Create your views here.
# services/views.py
from .models import Service
from django.shortcuts import render
from django.core.paginator import Paginator

def liste_services(request):
    # Récupérer le terme de recherche depuis la requête GET
    search_query = request.GET.get('search', '')  # Par défaut, la recherche est vide

    # Filtrer les services en fonction du terme de recherche
    # Par exemple, filtrer sur le nom ou la description
    services = Service.objects.filter(name__icontains=search_query)

    # Pagination : on définit 6 éléments par page
    paginator = Paginator(services, 6)  # 6 services par page
    page_number = request.GET.get('page')  # Numéro de page depuis l'URL
    page_obj = paginator.get_page(page_number)  # Obtenir la page actuelle

    # Renvoyer le rendu avec les services paginés et le terme de recherche
    return render(request, 'services/liste_services.html', {'page_obj': page_obj, 'search': search_query})

def detail_service(request, id):
    # Logique pour afficher un service détaillé par ID
    service = Service.objects.get(id=id)  # Récupérer le service par ID
    return render(request, 'services/detail_service.html', {'service': service})