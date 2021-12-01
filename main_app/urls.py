from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.WorkoutList.as_view(), name='workouts_index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='workouts_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
