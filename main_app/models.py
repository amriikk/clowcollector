from django.db import models
from django.urls import reverse

# Create your models here.

class Clow(models.Model):
    name = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    magic = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clows_detail', kwargs={ 'pk' : self.id })