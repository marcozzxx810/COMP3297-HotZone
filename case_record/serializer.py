from rest_framework import serializers
from case_record.models import CaseRecord
from visited_location.serializer import VisitedLocationRecordSerializer
from virus.serializer import VirusSerializer
from patient.serializer import PatientSerializer


class CaseRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    virus = VirusSerializer()
    visitedLoc = VisitedLocationRecordSerializer(many=True)

    class Meta:
        model = CaseRecord
        fields = ('__all__')
    
    def create(self, validated_data):
        patient_serializer = self.fields['patient']
        virus_serializer = self.fields['virus']
        visitedLoc_serializer = self.fields['visitedLoc']
        
        patient = patient_serializer.create(validated_data['patient'])
        virus = virus_serializer.create(validated_data['virus'])


        case_record = CaseRecord.objects.create(patient=patient,virus=virus)

        visitedLoc_validated_data = validated_data['visitedLoc']
        for each in visitedLoc_validated_data:
            each['case_record'] = case_record
        visitedLocs = visitedLoc_serializer.create(visitedLoc_validated_data)


        return case_record