
from django.db import models
from django.contrib.auth.models import User

class Travel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='travel_images/', null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    heritage_sites = models.TextField(null=True, blank=True)
    visitable_places = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=5)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
