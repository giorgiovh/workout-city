from django.shortcuts import render
from .models import Workout
from django.contrib.auth.views import LoginView
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST'
    #Here we create a 'user' form object including data from the browser
    
    
    
    
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', { 'workout': workout })