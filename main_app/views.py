from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello Planet</h1>')


def about(request):
    return render(request, 'about.html')


class Workout:  # This is the class & list function for creating workouts
    def __init__(self, muscle_grp, day_of_week, description, difficulty):
        self.muscle_grp = muscle_grp
        self.day_of_week = day_of_week
        self.description = description
        self.difficulty = difficulty


workouts = [
    Workout('Legs', 'Monday', '4x10 exercises', 4),
    Workout('Chest', 'Tuesday', '5x10 exercises', 2),
    Workout('Back', 'Monday', '5x15 exercises', 6),
    Workout('Shoulders and Arms', 'Friday', '5x10 exercises', 5),
]
