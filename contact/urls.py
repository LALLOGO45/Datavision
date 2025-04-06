# contact/urls.py
from django.urls import path
from . import views
from .views import send_email


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path("send_email/", send_email, name="send_email"),
]
