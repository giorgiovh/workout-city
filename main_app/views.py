from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Workout
from .forms import DidWorkoutForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['muscle_grp', 'day_of_week', 'description']
    success_url = '/workouts/'

class WorkoutUpdate(UpdateView):
  model = Workout
  fields = ['breed', 'description', 'age']

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'  


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Here we create a 'user' form object
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Add user to database
            login(request, user)  # Login the user
            return redirect('workouts_index')
        else:
            error_message = 'Invalid sign up - try again'
            # If a bad GET or POST request, render empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})

# @login_required
# class WorkoutList(ListView):
#     model = Workout
#     template_name = 'workouts/index.html'


@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    did_workout_form = DidWorkoutForm()
    return render(request, 'workouts/detail.html', {'workout': workout, 'did_workout_form': did_workout_form})
