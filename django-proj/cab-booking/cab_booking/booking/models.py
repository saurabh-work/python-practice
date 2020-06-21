from django.db import models

# Create your models here.


class Rider(models.Model):
    name = models.CharField(max_length=100)


class Driver(models.Model):
    name = models.CharField(max_length=100)


class Cab(models.Model):
    number = models.CharField(max_length=20)

    class Meta:
        ordering = ["-number"]


class CabDriver(models.Model):
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Booking(models.Model):
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)


# class CreateBookingDTO(object):
#     rider_id = models.CharField(max_length=100)