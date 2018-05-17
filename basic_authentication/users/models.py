from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # Create relationship (don't inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True) # looks in the media directory for the 'profile_pics' directory

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username
