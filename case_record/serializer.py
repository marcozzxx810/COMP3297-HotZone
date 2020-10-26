from rest_framework import serializers
from case_record.models import CaseRecord
from virus.serializer import VirusSerializer
from patient.serializer import PatientSerializer


class CaseRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    virus = VirusSerializer()

    class Meta:
        model = CaseRecord
        fields = ('__all__')
    
    def create(self, validated_data):
        patient_serializer = self.fields['patient']
        virus_serializer = self.fields['virus']
        
        patient = patient_serializer.create(validated_data['patient'])
        virus = virus_serializer.create(validated_data['virus'])


        case_record = CaseRecord.objects.create(patient=patient,virus=virus)

        return case_record