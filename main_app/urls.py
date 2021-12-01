from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.workouts_index, name='workouts_index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='workouts_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
