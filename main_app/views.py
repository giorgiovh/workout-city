from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Workout, Exercise, DidWorkout, Nutrition
from .forms import DidWorkoutForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


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


class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})


@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    exercises_workout_doesnt_have = Exercise.objects.exclude(
        id__in=workout.exercises.all().values_list('id'))
    did_workout_form = DidWorkoutForm()
    return render(request, 'workouts/detail.html', {
        'workout': workout,
        'did_workout_form': did_workout_form,
        'exercises': exercises_workout_doesnt_have
    })

@login_required
def add_didworkout(request, workout_id):
    form = DidWorkoutForm(request.POST)
    # validate form
    if form.is_valid():
        # don't save form until workout_id is assigned
        new_didworkout = form.save(commit=False)
        new_didworkout.workout_id = workout_id
        new_didworkout.save()
    return redirect('workouts_detail', workout_id=workout_id)


@login_required
def assoc_exercise(request, workout_id, exercise_id):
    Workout.objects.get(id=workout_id).exercises.add(exercise_id)
    return redirect('workouts_detail', workout_id=workout_id)


class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['muscle_grp', 'day_of_week', 'description']
    success_url = '/workouts/'


class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['muscle_grp', 'day_of_week', 'description']


class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'


class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = '__all__'


class ExerciseList(LoginRequiredMixin, ListView):
    model = Exercise


class ExerciseDetail(LoginRequiredMixin, DetailView):
    model = Exercise


class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = '__all__'


class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = '/exercises/'

class DidWorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = DidWorkout
    fields = ['date', 'did_workout']

class NutritionCreate(CreateView):
    model = Nutrition
    fields = '__all__'