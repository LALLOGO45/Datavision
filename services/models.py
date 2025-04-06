from django.db import models

# Create your models here.
# services/models.py
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image=models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return self.name
