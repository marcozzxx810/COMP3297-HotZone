from rest_framework import serializers
from visited_location.models import Location, VisitedLocationRecord


class LocationSerializer(serializers.Serializer):
    locNameEN = serializers.CharField(max_length=100)
    locAddressEN = serializers.CharField(max_length=100)
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

    def create(self, validated_data):
        loc_serializer = self.fields['visitedLoc']
        location_validated_data = validated_data.pop('visitedLoc')
        location = loc_serializer.create(location_validated_data)
        validated_data['visitedLoc'] = location

        vrecord = VisitedLocationRecord.objects.create(**validated_data)

        return vrecord