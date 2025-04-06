from django.db import models

# Create your models here.
# clients/models.py
from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    adresse = models.TextField()

    def __str__(self):
        return self.nom

class Projet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return self.nom
