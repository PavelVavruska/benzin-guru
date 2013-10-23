from django.db import models


class GasStation(models.Model):
    name = models.CharField(max_length=200)
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return self.name


class GasPrice(models.Model):
    station = models.ForeignKey(GasStation)
    date = models.DateTimeField('date published')
    price = models.FloatField()

    def __unicode__(self):
        return str(self.price) + '@' + str(self.date)


