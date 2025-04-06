# services/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.liste_services, name='liste_services'),
    path('services/<int:id>/', views.detail_service, name='detail_service'),
]

