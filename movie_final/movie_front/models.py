from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    review = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

