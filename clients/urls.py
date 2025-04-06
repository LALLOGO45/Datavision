# clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/<int:id>/', views.detail_client, name='detail_client'),
]
