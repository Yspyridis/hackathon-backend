from django.db import models
from django.contrib.postgres.fields import ArrayField

class Coordinate(models.Model):

    # model_type = models.CharField('Model', max_length=20)
    name = models.CharField('name', max_length=10)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
