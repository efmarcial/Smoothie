
from django.db import models



class image(models.Model):
    tilte = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    img = models.ImageField(upload_to = 'images/')