from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return 'first: %s, last: %s, email: %s' % (self.first_name, self.last_name, self.email)
