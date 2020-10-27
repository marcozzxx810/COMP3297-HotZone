from rest_framework import serializers
from case_record.models import CaseRecord
from virus.models import Virus
from virus.serializer import VirusSerializer
from patient.serializer import PatientSerializer


class CaseRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    
    virusName = serializers.CharField(max_length=100)
    caseDateofConfirm = serializers.DateField()
    caseType = serializers.CharField(max_length=50)

    class Meta:
        model = CaseRecord
        fields = ('patient', 'virusName', 'caseDateofConfirm', 'caseType')
    
    def validate_virusName(self, value):
        try: 
            virus = Virus.objects.get(virusName=value)
            return value
        except:
            raise serializers.ValidationError('Virus Not Found')
    
    def create(self, validated_data):
        patient_serializer = self.fields['patient']

        patientData = validated_data.pop('patient')
        patient = patient_serializer.create(patientData)
        virusNameStr = validated_data.pop('virusName')
        virus = Virus.objects.get(virusName=virusNameStr)

        case_record = CaseRecord.objects.create(**validated_data, patient=patient, virus=virus)

        return case_record