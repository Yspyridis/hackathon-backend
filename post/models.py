from django.db import models
from django.contrib.postgres.fields import ArrayField

class Coordinate(models.Model):

    # model_type = models.CharField('Model', max_length=20)
    name = models.CharField('name', max_length=10)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str('{0} {1} {2}' .format(self.name, self.x, self.y))
