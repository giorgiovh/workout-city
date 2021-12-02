from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
DIDYOU =  (
    ('Y', 'Worked out'),
    ('N', 'Did not workout')
)

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscle = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("exercises_detail", kwargs={"pk": self.id})

class Workout(models.Model):
    muscle_grp = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.muscle_grp

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={'workout_id': self.id})
    
    def worked_out_or_nah(self):
        return self.didworkout_set.filter(date=date.today()).count() >= 1

class DidWorkout(models.Model):
    date = models.DateField('Workout date')
    did_workout = models.CharField(
        max_length=1,
        choices=DIDYOU,
        default=DIDYOU[0][0]
        )
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_did_workout_display()} on {self.date}"

    def get_absolute_url(self):
        return reverse("workouts_detail", kwargs={'workout_id': self.workout.id})
    class Meta:
        ordering = ['-date']
        
class Nutrition(models.model):
    name_of_food = models.CharField(max_length=50)
    calories = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    meal = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
