from django.db import models

# Create your models here.
class Tracker(models.Model):
    content = models.TextField()
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)