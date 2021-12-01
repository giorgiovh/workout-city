from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.workouts_index, name='workouts_index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='workouts_detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
    path('workouts/<int:workout_id>/add_didworkout/', views.add_didworkout, name='add_didworkout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
    path('exercises/', views.ExerciseList.as_view(), name='exercises_index')
]
