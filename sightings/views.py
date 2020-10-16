from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Squirrels
from .forms import SightingsForm

# Create your views here.
def home(request):
    return render(request,'sightings/home.html')
