from django.db import models
from case_record.models import CaseRecord

# Create your models here.

class Location(models.Model):
    locNameEN = models.CharField(max_length=100)
    locAddressEN = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()

    def __str__(self):
        return "%s" % self.locNameEN

class VisitedLocationRecord(models.Model):
    visitedLocDateFrom = models.DateField()
    visitedLocDateTo = models.DateField()
    visitedLocCategory = models.CharField(max_length=50)
    case_record = models.ForeignKey(CaseRecord, on_delete=models.CASCADE, null=True)
    visitedLoc = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
