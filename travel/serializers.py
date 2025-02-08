from rest_framework import serializers
from .models import Destination, TravelPackage

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class TravelPackageSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer()

    class Meta:
        model = TravelPackage
        fields = ['id', 'name', 'destination', 'price', 'duration_days', 'available']

    def create(self, validated_data):
        destination_data = validated_data.pop('destination')
        # Create the destination if it doesn't exist
        destination = Destination.objects.create(**destination_data)
        # Create the travel package with the new destination
        travel_package = TravelPackage.objects.create(destination=destination, **validated_data)
        return travel_package
