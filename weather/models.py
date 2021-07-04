from django.contrib.gis.db import models

class Place(models.Model):
    place = models.CharField(max_length=100)
    location = models.PointField()

