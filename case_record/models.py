from django.db import models
from patient.models import Patient
from virus.models import Virus


# Create your models here.
class CaseRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    virus = models.ForeignKey(
        Virus,
        on_delete=models.CASCADE,
    )