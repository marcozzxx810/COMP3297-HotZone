from rest_framework import serializers
from case_record.models import CaseRecord
from visited_location.models import Location, VisitedLocationRecord


class LocationSerializer(serializers.Serializer):
    locNameEN = serializers.CharField(max_length=100)
    locAddressEN = serializers.CharField(max_length=100, allow_blank=True)
    locX = serializers.FloatField()
    locY = serializers.FloatField()
    
    def create(self, validated_data):
        return Location.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        pass

class VisitedLocationRecordSerializer(serializers.Serializer):
    visitedLocDateFrom = serializers.DateField()
    visitedLocDateTo = serializers.DateField()
    visitedLocCategory = serializers.CharField(max_length=50)
    visitedLoc = LocationSerializer()
    case_record = serializers.IntegerField()

    def validate_case_record(self, value):
        try: 
            case = CaseRecord.objects.get(id=value)
            return value
        except:
            raise serializers.ValidationError('Case Record Not Found')

    def create(self, validated_data):
        loc_serializer = self.fields['visitedLoc']
        location_validated_data = validated_data.pop('visitedLoc')
        location = loc_serializer.create(location_validated_data)
        validated_data['visitedLoc'] = location

        casePK = validated_data.pop('case_record')
        case = CaseRecord.objects.get(id=casePK)
        validated_data['case_record'] = case

        vrecord = VisitedLocationRecord.objects.create(**validated_data)

        return vrecord