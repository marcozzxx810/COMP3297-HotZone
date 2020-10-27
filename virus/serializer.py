from rest_framework import serializers
from virus.models import Virus


class VirusSerializer(serializers.Serializer):
    virusName = serializers.CharField(max_length=100)
    virusCommonName = serializers.CharField(max_length=100)
    virusDay = serializers.IntegerField()

    def validate_virusName(self, value):
        virus = Virus.objects.filter(virusName=value)
        if len(virus):
            raise serializers.ValidationError(f'Virus: {value} already in used')
        else:
            return value

    def create(self, validated_data):
        return Virus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass