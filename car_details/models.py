from django.db import models
import datetime
class Car(models.Model):
    id = models.AutoField(primary_key = True)
    car_number = models.CharField(max_length=50)
    car_intime = models.CharField(max_length=10)
    car_outtime = models.CharField(max_length=10)
    car_date = models.DateTimeField()
    # Is_parking = models.BooleanField()
    def __str__(self):
        return self.car_number

class Parking(models.Model):
    id = models.AutoField(primary_key = True)
    car_id = models.ForeignKey(Car,null=True, blank=True,on_delete=models.SET_NULL)
    position = models.IntegerField()
