from django.db import models
from django.contrib.postgres.fields import ArrayField

class Coordinate(models.Model):

    # model_type = models.CharField('Model', max_length=20)
    name = models.CharField('name', max_length=10)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str('{0} {1} {2}' .format(self.name, self.x, self.y))


class farms(models.Model):

    farm_name = models.CharField(max_length=500)
    corp_type = models.CharField(max_length=500)
    cords = models.CharField(max_length=500)

    farm_center = models.CharField(max_length=500)
    sustainable = models.BooleanField(blank=True)

    def __str__(self):
        return str('{0} {1} {2}' .format(self.farm_name, self.corp_type, self.sustainable))
