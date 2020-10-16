
from django.forms import ModelForm

from .models import Squirrels


class SightingsForm(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'
