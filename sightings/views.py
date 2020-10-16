from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Squirrels
from .forms import SquirrelForm

# Create your views here.
def homepage_view(request):
    return render(request,'sightings/homepage.html')
