from rest_framework import serializers

from .models import *


class CabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cab
        fields = ['number']


class RiderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rider
        fields = ['name', 'pk']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['cab', 'rider']


# class CreateBookingSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CreateBookingDTO
#         fields = ['rider_id']