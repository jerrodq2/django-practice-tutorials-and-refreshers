from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    text = models.CharField(max_length=1000)
