from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from car_details.models import Car,Parking
import datetime
# Create your views here.
def index(request):
    if request.method =='POST':
        now = datetime.datetime.now()
        car = Car()
        car.car_number = request.POST.get('car_number')
        car.car_intime = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        car.car_outtime = ''
        car.car_date = now
        car.save()
        try:
            availableParking = Parking.objects.exclude(car_id__isnull=False)[0]
            availableParking.car_id = car
            availableParking.save()
        except :
            print("Http 404 Not found")
    if(Parking.objects.count()>0):
        parkings = Parking.objects.all()
    else:
        for i in range(20):
            parking = Parking()
            parking.position = i+1
            parking.save()
        parkings = Parking.objects.all()

    cars = Car.objects.all()
    return render(request,'index.html',{
        'cars':cars,
        'parkings':parkings
    })




