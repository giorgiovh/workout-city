from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello Planet</h1>')


def about(request):
    return render(request, 'about.html')


class Workout: #This is the class & list function for creating workouts
    def __init__(self, muscle_grp, day_of_week, description, difficulty):