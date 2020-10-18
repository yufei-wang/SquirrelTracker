from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Squirrels
from .forms import SightingsForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
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
    s = Squirrels.objects.filter(Unique_Squirrel_Id=unique_squirrel_id).first()
    squirrels = model_to_dict(s)
    context= {'squirrels':squirrels}
    return render(request, 'sightings/squirrel_id.html',context)

def add(request):
    if request.method == "POST":
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/sightings/')
    else:
        form = SightingsForm()
    context = {
            'form':form,
        }
    return render(request,'sightings/add.html',context)

def stats(request):
    num_sightings = Squirrels.objects.all().count()
    num_morning_sight = Squirrels.objects.filter(Shift='AM').count()
    num_adult = Squirrels.objects.filter(Age='Adult').count()
    num_aboveground = Squirrels.objects.filter(Location='Above Ground').count()
    num_eating = Squirrels.objects.filter(Eating=True).count()
    context = {

        'num_sightings': num_sightings,

        'num_morning_sight': num_morning_sight,

        'num_adult': num_adult,

        'num_aboveground': num_aboveground,

        'num_eating': num_eating,

    }
    return render(request, 'sightings/stats.html', context)

