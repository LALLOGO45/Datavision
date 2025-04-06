# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.liste_articles, name='liste_articles'),
    path('blog/<int:id>/', views.detail_article, name='detail_article'),
]
