from django.urls import path
from . import views

urlpatterns = [path('', views.create_workout, name='create_workout'),
               path('search/', views.search_workouts, name='search_workouts'),
               ]
