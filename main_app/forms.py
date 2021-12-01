from django.forms import ModelForm
from .models import DidWorkout

class DidWorkoutForm(ModelForm):
  class Meta:
    model = DidWorkout
    fields = ['date', 'did_workout']