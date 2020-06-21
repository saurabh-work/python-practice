import random

from django.shortcuts import render
# from django.http import response, HttpResponse
from django.views.generic import View
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .models import *

# random cab
# online cab
# custom sql query
# logs
# transactions
# synchronization
# sentry
# newrelic
# container
# k8s
#


class CabViewSet(viewsets.ModelViewSet):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer
    permission_classes = [permissions.IsAuthenticated]


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def book_cab(self, request, pk=None):
        rider = self.get_object()
        cabs = Cab.objects.all()
        cab = random.choice(cabs)

        booking = Booking()
        booking.cab = cab
        booking.rider = rider
        booking.save()
        # serializer = BookingSerializer(booking)

        # return Response(serializer.data)
        return Response({'status': 'password set'})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

