from rest_framework import serializers
from virus.models import Virus


class VirusSerializer(serializers.Serializer):
    virusName = serializers.CharField(max_length=100)
    virusCommonName = serializers.CharField(max_length=100)
    virusDay = serializers.IntegerField()

    def create(self, validated_data):
        return Virus.objects.get_or_create(**validated_data)[0]

    def update(self, instance, validated_data):
        pass