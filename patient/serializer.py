from rest_framework import serializers
from patient.models import Patient


class PatientSerializer(serializers.Serializer):
    patientName = serializers.CharField(max_length=100)
    patientHKID = serializers.CharField(max_length=20)
    patientBDay = serializers.DateField()

    def create(self, validated_data):
        return Patient.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        pass