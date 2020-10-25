from django.db import models


class Patient(models.Model):
    patientName = models.CharField(max_length=100)
    patientHKID = models.CharField(max_length=20)
    patientBDay = models.DateField()

    def __str__(self):
        return "%s" % self.patientName