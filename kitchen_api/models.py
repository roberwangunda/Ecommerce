from django.db import models

# Create your models here.

class Kitchen(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.CharField(max_length=100)