from django.db import models


class GasStation(models.Model):
    name = models.CharField(max_length=200)
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return self.name
