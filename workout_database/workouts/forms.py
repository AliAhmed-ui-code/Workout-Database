from django import forms
from . import models

class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = ['name', 'muscle_group', 'sets', 'reps', 'weight', 'incline', 'equipment' ]