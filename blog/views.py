from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator

def liste_articles(request):
    search_query = request.GET.get('search', '')  # Par défaut, la recherche est vide

    # Filtrer les services en fonction du terme de recherche
    # Par exemple, filtrer sur le nom ou la description
    articles = Article.objects.filter(titre__icontains=search_query)

    # Pagination : on définit 6 éléments par page
    paginator = Paginator(articles, 6)  # 6 services par page
    page_number = request.GET.get('page')  # Numéro de page depuis l'URL
    page_obj = paginator.get_page(page_number)  # Obtenir la page actuelle

    # Renvoyer le rendu avec les services paginés et le terme de recherche
    return render(request, 'blog/liste_articles.html', {'page_obj': page_obj, 'search': search_query})


def detail_article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/detail_article.html', {'article': article})
