from django.contrib import admin
from .models import Nutrition, Workout, DidWorkout, Exercise

# Register your models here
admin.site.register(Workout)
admin.site.register(DidWorkout)
admin.site.register(Exercise)
admin.site.register(Nutrition)

# test comment


