from django.db import models


class Virus(models.Model):
    virusName = models.CharField(max_length=100)
    virusCommonName = models.CharField(max_length=100)
    virusDay = models.IntegerField()

    def __str__(self):
        return "%s" % self.virusName