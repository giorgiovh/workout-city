from django.db import models

# Create your models here.


class Workout(models.Model):
    muscle_grp = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.muscle_grp
