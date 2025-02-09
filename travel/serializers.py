from rest_framework import serializers
from .models import Destination, TravelPackage, CustomUser

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

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        # Create a new user and hash the password
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user