from django.shortcuts import render
from .models import Workout
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})


class Workout:  # This is the class & list function for creating workouts
    def __init__(self, muscle_grp, day_of_week, description):
        self.muscle_grp = muscle_grp
        self.day_of_week = day_of_week
        self.description = description
        


workouts = [
    Workout('Legs', 'Monday', '4x10 exercises'),
    Workout('Chest', 'Tuesday', '5x10 exercises'),
    Workout('Back', 'Monday', '5x15 exercises'),
    Workout('Shoulders and Arms', 'Friday', '5x10 exercises'),
]
