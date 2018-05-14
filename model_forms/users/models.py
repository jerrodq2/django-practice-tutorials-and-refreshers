from django.db import models

# Create your models here.
class User(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length=128, blank = True)
    email = models.EmailField(max_length=254,unique=True)
    summary = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return 'First: %s, Email: %s' % (self.first, self.email)
