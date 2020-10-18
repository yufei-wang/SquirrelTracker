from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Squirrels
from .forms import SightingsForm

# Create your views here.
def home(request):
    return render(request,'sightings/home.html')


def map(request):
    squirrels = Squirrels.objects.all()
    res = []
    for s in squirrels:
        new_dict = {'latitude':s.Latitude,'longitude':s.Longitude}
        res.append(new_dict)
    return render(request,'sightings/map.html',context={'sightings':res})

def sightings(request):
    squirrels = Squirrels.objects.all()
    squirrels_id = []
    for i in squirrels:
        new_dict = {'unique_squirrel_id':i.Unique_Squirrel_Id,'date':i.Date} 
        squirrels_id.append(new_dict)
    return render(request,'sightings/sightings.html',context={'sightings':squirrels_id})

def squirrel_id(request,unique_squirrel_id):
    context = {'unique-squirrel-id' : unique_squirrel_id}
    return render(request, 'sightings/squirrel_id.html',context)
