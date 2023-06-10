from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    name_owner = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} , owner:{self.name_owner}"


class Car(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Workshop(models.Model):
    name = models.CharField(max_length=50)
    year_of_establishment = models.IntegerField()
    old_timer = models.BooleanField()

    def __str__(self):
        return self.name

class ScheduledRepair(models.Model):
    code = models.CharField(max_length=10)
    date_reported = models.DateField(auto_now_add=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/",null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class WorkshopManufacturer(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


